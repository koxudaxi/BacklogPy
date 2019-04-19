"""
    This code generate backlog api client for python.
    Python 3.7 or or later is required for the code generator.
"""
from __future__ import annotations

import os
import re
import time
from enum import Enum
from logging import INFO, getLogger, Logger
from typing import Any, Dict, Generator, List, Optional, Pattern, Type, Union, Tuple, Set

import requests
from autopep8 import fix_code, parse_args
from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import Response

logger: Logger = getLogger(__name__)
logger.setLevel(INFO)

PACKAGE_NAME: str = 'BacklogPy'

DOWNLOAD_WAIT_TIME: int = 1
DATA_DIR: str = 'download'
API_ROOT: str = '/api/v2'

CODING: str = '# coding: utf-8'

AUTO_GENERATE_MESSAGE: str = \
    '''"""
    This file was created by Backlog APIGenerator
"""
'''

FUTURE_IMPORT: str = 'from __future__ import unicode_literals, absolute_import'

DEPRECATED_MODULE_IMPORT: str = 'from deprecated import deprecated'

BACKLOG_TEMPLATE: str = \
    f'''{CODING}
    
{AUTO_GENERATE_MESSAGE}

{FUTURE_IMPORT}

from {PACKAGE_NAME}.api import *


class Backlog({{objects}}):
    pass
'''

API_CLASS_TEMPLATE: str = \
    f'''{CODING}

{AUTO_GENERATE_MESSAGE}

{FUTURE_IMPORT}
{{{{module_import}}}}
from {PACKAGE_NAME}.base import BacklogBase


class {{space_name}}(BacklogBase):
    def __init__(self, space_id, api_key):
        super({{space_name}}, self).__init__(space_id, api_key)
'''

API_METHOD_TEMPLATE: str = \
    '''
    def {api_name}(self{method_args}):
        """{method_doc}{args_doc}
        :return:  requests Response object 
        :rtype: requests.Response
        """
        
        {parameter_assignment}
        
        return self._request({api_call_args})
'''

INIT_PY_TEMPLATE: str = \
    f'''{CODING}

{AUTO_GENERATE_MESSAGE}

{{import_block}}

__all__ = [{{all_block}}]

'''

DEVELOPER_URL: str = 'https://developer.nulab-inc.com'
OVERVIEW_URL: str = 'https://developer.nulab-inc.com/docs/backlog/'

DEPRECATED_WORD: str = '※ Deprecated API. '
DEPRECATED_TEMPLATE: str = '''
    @deprecated(reason="{reason}")'''


class Parameter:
    _UNDER_SCORER1: Pattern = re.compile(r'(.)([A-Z][a-z]+)')
    _UNDER_SCORER2: Pattern = re.compile('([a-z0-9])([A-Z])')
    _REQUIRED_RE: Pattern = re.compile(r' \([Rr]equired\)$')

    _LIST_RE: Pattern = re.compile(r'\[\]')

    class Type(Enum):
        INT: Tuple[str, str] = ('Number', 'int')
        STR: Tuple[str, str] = ('String', 'str')
        BOOL: Tuple[str, str] = ('Boolean', 'bool')
        DICT: Tuple[str, str] = ('dict', 'dict')
        STR_LIST: Tuple[str, str] = ('list[String]', 'list[str] or str')
        INT_LIST: Tuple[str, str] = ('list[Number]', 'list[int] or int')

        _doc: str = ''
        _value: str = ''

        def __new__(cls, *values: Union[str, List[str]]) -> 'Type':
            obj: Type = object.__new__(cls)
            obj._value_ = values[0]
            if len(values) > 1:
                obj._doc = values[1]
            return obj

        @property
        def doc(self) -> str:
            return self._doc

    @classmethod
    def camel_to_snake(cls, name: str) -> str:
        subbed = cls._UNDER_SCORER1.sub(r'\1_\2', name)
        return cls._UNDER_SCORER2.sub(r'\1_\2', subbed).lower()

    @classmethod
    def convert_to_correct_name(cls, name: str) -> str:
        if name == 'id':
            name: str = '_id'
        if re.search(cls._LIST_RE, name):
            name = re.sub(cls._LIST_RE, '', name)
        if re.search(cls._REQUIRED_RE, name):
            name = re.sub(cls._REQUIRED_RE, '', name)

        return cls.camel_to_snake(name)

    def __init__(self, raw_name: str, raw_type: str,
                 description: Optional[str] = None,
                 force_required: bool = False) -> None:

        self.name: str = self.convert_to_correct_name(raw_name)

        self.description: str = description if description else raw_name

        if re.search(self._LIST_RE, raw_name):
            self.type: Parameter.Type = self.Type(f'list[{raw_type}]')
        else:
            self.type: Parameter.Type = self.Type(raw_type)

        if force_required or re.search(self._REQUIRED_RE, raw_name):
            self.required: bool = True
        else:
            self.required = False

        self.key: str = re.sub(self._REQUIRED_RE, '', raw_name)

    @property
    def method_arg(self) -> str:
        if self.required:
            return f'{self.name}'

        return f'{self.name}=None'

    @property
    def doc(self) -> str:
        return f':param {self.type.doc} {self.name}: {self.description}'

    def __lt__(self, other: 'Parameter') -> bool:
        return self.name < other.name


Parameters = List[Parameter]


def _get_api_urls(developer_url: str = DEVELOPER_URL,
                  overview_url: str = OVERVIEW_URL) -> Generator[str,
                                                                 None, None]:
    bs: BeautifulSoup = _get_bs_from_url(overview_url)
    api_list: Tag = bs.find('optgroup', label='Backlog API')
    for api in api_list.find_all('option'):
        yield developer_url + api['value']


def _get_bs_from_file(base_dir: str = DATA_DIR) -> Generator[BeautifulSoup,
                                                             None, None]:
    if not os.path.isdir(base_dir):
        raise Exception(f'Not Found Directory: {base_dir}')

    for file in os.listdir(base_dir):
        with open(os.path.join(base_dir, file)) as f:
            yield BeautifulSoup(f.read(), "lxml")


def _get_bs_from_url(target_url: str) -> BeautifulSoup:
    response: Response = requests.get(target_url)
    return BeautifulSoup(response.content, 'lxml')


def _get_bs_from_web(download_wait_time: int = DOWNLOAD_WAIT_TIME) -> \
        Generator[BeautifulSoup, None, None]:
    for url in _get_api_urls():
        time.sleep(download_wait_time)
        yield _get_bs_from_url(url)


def _create_init_py(space_list: List[str]) -> str:
    all_list: List[str] = []
    import_list: List[str] = []
    for space in space_list:
        import_list.append(
            f'from {PACKAGE_NAME}.api.{space} import {space.title()}')
        all_list.append(f'\'{space.title()}\'')
    return INIT_PY_TEMPLATE.format(import_block='\n'.join(import_list),
                                   all_block=','.join(all_list))


def _create_backlog_py(space_list: List[str]) -> str:
    objects: str = ', '.join([o.title() for o in space_list])
    return BACKLOG_TEMPLATE.format(objects=objects)


def _write_code(code: str, base_path: str, file_name: str) -> None:
    file_path: str = os.path.join(base_path, file_name)
    logger.info(f'write {file_path}')
    fixed_init_py: str = fix_code(code,
                                  options=parse_args(['--aggressive', '--aggressive', '']))

    with open(file_path, 'w') as f:
        f.write(fixed_init_py)


def _create_dir(path: str) -> None:
    if os.path.exists(path):
        if not os.path.isdir(path):
            raise Exception(f"File Exists: {path}")
    else:
        os.mkdir(path)


def _create_api_from_bs_generator(
        bs_generator: Generator[BeautifulSoup, None, None],
        output_dir: str = PACKAGE_NAME) -> None:
    api_path = f'{output_dir}/api'

    stock: Dict[str, Any] = {}
    for api in sorted(APIGenerator(bs) for bs in bs_generator):
        if api.space_name not in stock:
            stock[api.space_name] = {}
            stock[api.space_name]['class'] = api.create_api_class()
            stock[api.space_name]['method'] = []
            stock[api.space_name]['module']: Set[str] = set()
        stock[api.space_name]['method'].append(api.create_api_method())
        if api.has_strict_method:
            stock[api.space_name]['method'].append(
                api.create_api_method(strict=True))
        stock[api.space_name]['module'].update(api.modules)

    _create_dir(api_path)

    for space, api_dict in stock.items():
        if api_dict['module']:
            modules: str = '\n' + '\n'.join(module for module in api_dict['module']) + '\n'
        else:
            modules = ''
        class_code: str = api_dict['class'].format(module_import=modules)
        method_code = class_code + ''.join(api_dict['method'])
        _write_code(method_code, api_path, f'{space}.py')

    sorted_stock_keys: List[str] = sorted(stock.keys())

    init_py: str = _create_init_py(sorted_stock_keys)
    _write_code(init_py, api_path, '__init__.py')

    backlog_py: str = _create_backlog_py(sorted_stock_keys)
    _write_code(backlog_py, output_dir, 'backlog.py')


def create_api_from_file(data_dir: str = DATA_DIR) -> None:
    bs_generator: Generator[BeautifulSoup, None, None] = _get_bs_from_file(data_dir)
    _create_api_from_bs_generator(bs_generator)


def crete_api_from_web(download_wait_time: int = DOWNLOAD_WAIT_TIME) -> None:
    bs_generator: Generator[BeautifulSoup, None, None] = _get_bs_from_web(download_wait_time)
    _create_api_from_bs_generator(bs_generator)


def download_doc_file(data_dir: str,
                      download_wait_time: int = DOWNLOAD_WAIT_TIME) -> None:
    _create_dir(data_dir)
    for api_url in _get_api_urls():
        r: Response = requests.get(api_url)
        time.sleep(download_wait_time)
        file_name: str = api_url.split('/')[-1]
        logger.info('write file: {sleep}')
        with open(os.path.join(data_dir, file_name + '.html'), 'wb') as f:
            f.write(r.content)


class APIGenerator:
    newline_and_indent: str = '\n        '

    def __init__(self, bs: BeautifulSoup) -> None:
        self.bs: BeautifulSoup = bs
        self._method_type: str = ''
        self._api_path: str = ''
        self._url_parameters: Parameters = []
        self._form_parameters: Parameters = []
        self._query_parameters: Parameters = []
        self._short_path: str = ''
        self._space_name: str = ''
        self._api_name: str = ''
        self._api_description: str = ''
        self._deprecated_message: str = ''
        self._modules: Set[str] = set()

    def __lt__(self, other: 'APIGenerator') -> bool:
        return self.api_name < other.api_name

    @property
    def has_strict_method(self) -> bool:
        if self.form_parameters or self.query_parameters:
            return True
        else:
            return False

    @property
    def api_name(self) -> str:
        if self._api_name:
            return self._api_name
        raw_api_name: Tag = self.bs.find('h2')['id']
        self._api_name: str = raw_api_name.replace('-', '_')
        return self._api_name

    @property
    def api_description(self) -> str:
        if self._api_description:
            return self._api_description
        api_name_element: Tag = self.bs.find('h2')
        link: str = ''
        for element in api_name_element.next_elements:
            if element.name == 'p':
                self._api_description: str = element.text.replace('\n', ' ')
                if element.a:
                    link = element.a['href']
                    self._api_description += link
                if DEPRECATED_WORD in element.text:
                    self._deprecated_message = element.text.split(DEPRECATED_WORD)[1].replace('\n', ' ') + link
                    self._modules.add(DEPRECATED_MODULE_IMPORT)
                return self._api_description
        raise Exception('Not Found Description')

    @property
    def method_type(self) -> str:
        if self._method_type:
            return self._method_type
        for api_path in self.bs.find_all('h3', id='method'):
            for element in api_path.next_elements:
                if element.name == 'code':
                    self._method_type: str = element.contents[0].replace(' \n', '')
                    return self._method_type
        raise Exception('Not Found Method')

    @property
    def api_path(self) -> str:
        if self._api_path:
            return self._api_path
        for api_path in self.bs.find_all('h3', id='url'):
            for element in api_path.next_elements:
                if element.name == 'code':
                    self._api_path: str = element.contents[0].replace(' \n', '')
                    return self._api_path
        raise Exception('Not Found API Path')

    @property
    def short_path(self) -> str:
        if self._short_path:
            return self._short_path
        self._short_path: str = self.api_path.replace(API_ROOT, '')
        return self._short_path

    @property
    def space_name(self) -> str:
        if self._space_name:
            return self._space_name
        self._space_name = self.short_path.split('/')[1]
        return self._space_name

    @property
    def url_parameters(self) -> Parameters:
        if self._url_parameters:
            return self._url_parameters
        self._url_parameters: Parameters = self._get_parameters('url-parameters', True)
        return self._url_parameters

    def _get_parameters(self, html_id: str,
                        force_required: bool = False) -> Parameters:
        parameters: Parameters = []

        for h3 in self.bs.find_all('h3', id=html_id):
            for element in h3.next_elements:
                if element.name == 'thead':
                    th = element.find('th')
                    if len(th.contents[0]) and th.contents[
                        0] != 'Parameter Name':
                        parameters = [Parameter(*[th.contents[0]
                                                  for th in
                                                  element.find_all('th')
                                                  if th.contents],
                                                force_required=force_required)]
                elif element.name == 'tbody':
                    tbody: Tag = element
                    lines = tbody.find_all('tr')
                    return parameters + \
                           [Parameter(*[td.contents[0]
                                        for td in
                                        line.find_all('td')
                                        if td.contents],
                                      force_required=force_required)
                            for line in lines]

        return []

    @property
    def form_parameters(self) -> Parameters:
        if self._form_parameters:
            return self._form_parameters
        self._form_parameters = self._get_parameters('form-parameters')
        return self._form_parameters

    @property
    def query_parameters(self) -> Parameters:
        if self._query_parameters:
            return self._query_parameters
        self._query_parameters = self._get_parameters('query-parameters')
        return self._query_parameters

    def _create_api_call_args(self) -> str:
        api_call_args: List[str] = []

        if self.url_parameters:
            path = re.sub(':.[^/]+', '{}', self.short_path)
            parameter_names = [url_parameter.name
                               for
                               url_parameter in
                               self.url_parameters]
            parameter_args: str = ', '.join(parameter_names)
            api_call_args.append(f'\'{path}\'.format({parameter_args})')
        else:
            api_call_args.append(f'\'{self.short_path}\'')

        api_call_args.append(f'method=\'{self.method_type}\'')

        if self.query_parameters:
            api_call_args.append('query_parameters=query_parameters')

        if self.form_parameters:
            api_call_args.append('form_parameters=form_parameters')

        return ', '.join(api_call_args)

    def _create_method_args(self, strict: bool = False) -> str:
        method_args: List[str] = []
        method_kwargs: List[str] = []

        for url_parameter in self.url_parameters:
            method_args.append(url_parameter.method_arg)

        if self.query_parameters:
            if strict:
                for query_parameter in self.query_parameters:
                    if query_parameter.required:
                        method_args.append(query_parameter.method_arg)
                    else:
                        method_kwargs.append(query_parameter.method_arg)
            else:
                method_args.append('query_parameters')

        if self.form_parameters:
            if strict:
                for form_parameter in self.form_parameters:
                    if form_parameter.required:
                        method_args.append(form_parameter.method_arg)
                    else:
                        method_kwargs.append(form_parameter.method_arg)
            else:
                method_args.append('form_parameters')
        arg_string: str = ', '.join(method_args + method_kwargs)
        if arg_string:
            return f', {arg_string}'
        else:
            return ''

    def _create_args_doc(self, strict: bool = False) -> str:

        args_doc: List[str] = []

        for url_parameter in self.url_parameters:
            args_doc.append(url_parameter.doc)

        if self.query_parameters:
            if strict:
                for query_parameter in self.query_parameters:
                    args_doc.append(query_parameter.doc)
            else:
                args_doc.append(
                    Parameter('query_parameters', 'dict',
                              'query_parameters').doc)

        if self.form_parameters:
            if strict:
                for form_parameters in self.form_parameters:
                    args_doc.append(form_parameters.doc)
            else:
                args_doc.append(
                    Parameter('form_parameters', 'dict',
                              'form_parameters').doc)

        if args_doc:
            return self.newline_and_indent + \
                   self.newline_and_indent.join(args_doc) \
                   + self.newline_and_indent
        else:
            return ''

    def _create_parameter_assignment(self) -> str:
        parameter_assignment: List[str] = []

        def create_parameter_dict(parameters: Parameters) -> str:
            def get_key_value_pair(parameter: Parameter) -> str:
                if parameter.type == Parameter.Type.BOOL:
                    parameter_variable = f'self._bool_to_str({parameter.name})'
                else:
                    parameter_variable = parameter.name
                return f'\'{parameter.key}\': {parameter_variable}'

            key_values = f',{self.newline_and_indent}    '.join(
                [get_key_value_pair(p) for p in parameters])

            return f'{{{self.newline_and_indent}{key_values}' \
                   f'{self.newline_and_indent}}}'

        if self.query_parameters:
            query_dict = create_parameter_dict(self.query_parameters)
            parameter_assignment.append(f'query_parameters = {query_dict}')

        if self.form_parameters:
            form_dict = create_parameter_dict(self.form_parameters)
            parameter_assignment.append(f'form_parameters = {form_dict}')

        return '\n\n'.join(parameter_assignment)

    def _create_method_doc(self) -> str:
        newline_and_indent: str = '\n        '
        return newline_and_indent + self.api_description + newline_and_indent

    def create_api_class(self) -> str:
        return API_CLASS_TEMPLATE.format(
            space_name=self.space_name.title()
        )

    @property
    def deprecated(self) -> bool:
        if self._deprecated_message:
            return True
        return False

    @property
    def modules(self) -> Set[str]:
        return self._modules

    def create_api_method(self, strict: bool = False) -> str:
        if strict or not self.has_strict_method:
            parameter_assignment = self._create_parameter_assignment()
            api_name = self.api_name
        else:
            parameter_assignment = ''
            api_name = f'{self.api_name}_raw'

        api_method: str = API_METHOD_TEMPLATE.format(
            method_args=self._create_method_args(strict),
            args_doc=self._create_args_doc(strict),
            method_doc=self._create_method_doc(),
            api_name=api_name,
            parameter_assignment=parameter_assignment,
            api_call_args=self._create_api_call_args())

        if self.deprecated:
            deprecated_decorator: str = DEPRECATED_TEMPLATE.format(reason=self._deprecated_message)
            return deprecated_decorator + api_method

        return api_method


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(prog='API Generator')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_crete = subparsers.add_parser('create',
                                         help='create backlog api from html')
    parser_crete.add_argument('--data_dir', type=str, default=DATA_DIR,
                              required=False)
    parser_crete.set_defaults(func=create_api_from_file)
    parser_download = subparsers.add_parser('download',
                                            help='download backlog '
                                                 'document html')
    parser_download.add_argument('--data_dir', type=str, default=DATA_DIR,
                                 required=False)
    parser_download.add_argument('--download_wait_time', type=int, default=1,
                                 required=False)
    parser_download.set_defaults(func=download_doc_file)

    args = parser.parse_args()

    args_dict = vars(args).copy()
    if args_dict:
        del args_dict['func']
        args.func(**args_dict)
    else:
        parser.print_help()
