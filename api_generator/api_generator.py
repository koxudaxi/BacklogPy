"""
    This code generate backlog api client for python.
    Python 3.6 or or later is required for the code generator.
"""

import os
import re
import time
from logging import getLogger, INFO

import requests
from autopep8 import parse_args, fix_code
from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import List, Generator, Dict, Any

logger = getLogger(__name__)
logger.setLevel(INFO)

Parameters = List[List[str]]

PACKAGE_NAME = 'BacklogPy'

DOWNLOAD_WAIT_TIME = 1
DATA_DIR = 'download'
API_ROOT = '/api/v2'

CODING = '# coding: utf-8'

AUTO_GENERATE_MESSAGE = \
    '''"""
    This file was created by Backlog APIGenerator
"""
'''

FUTURE_IMPORT = 'from __future__ import unicode_literals, absolute_import'

BACKLOG_TEMPLATE = \
    f'''{CODING}
    
{AUTO_GENERATE_MESSAGE}

{FUTURE_IMPORT}

from {PACKAGE_NAME}.api import *


class Backlog({{objects}}):
    pass
'''

API_CLASS_TEMPLATE = \
    f'''{CODING}

{AUTO_GENERATE_MESSAGE}

{FUTURE_IMPORT}

from {PACKAGE_NAME}.base import BacklogBase


class {{space_name}}(BacklogBase):
    def __init__(self, space_id, api_key):
        super({{space_name}}, self).__init__(space_id, api_key)
'''

API_METHOD_TEMPLATE = \
    '''
    def {api_name}(self{method_args}):
        """{method_doc}{args_doc}
        :return:  requests Response object 
        :rtype requests.Response
        """
        return self._request({api_call_args})
'''

INIT_PY_TEMPLATE = \
    f'''{CODING}

{AUTO_GENERATE_MESSAGE}

{{import_block}}

__all__ = [{{all_block}}]

'''

DEVELOPER_URL = 'https://developer.nulab-inc.com'
OVERVIEW_URL = 'https://developer.nulab-inc.com/docs/backlog/'


def _get_api_urls(developer_url: str = DEVELOPER_URL,
                  overview_url: str = OVERVIEW_URL) -> Generator[
    str, None, None]:
    bs = _get_bs_from_url(overview_url)
    api_list = bs.find('optgroup', label='Backlog API')
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
    response = requests.get(target_url)
    return BeautifulSoup(response.content, 'lxml')


def _get_bs_from_web(download_wait_time: int = DOWNLOAD_WAIT_TIME) -> \
        Generator[BeautifulSoup, None, None]:
    for url in _get_api_urls():
        time.sleep(download_wait_time)
        yield _get_bs_from_url(url)


def _create_init_py(space_list: List[str]) -> str:
    all_list = []
    import_list = []
    for space in space_list:
        import_list.append(
            f'from {PACKAGE_NAME}.api.{space} import {space.title()}')
        all_list.append(f'\'{space.title()}\'')
    return INIT_PY_TEMPLATE.format(import_block='\n'.join(import_list),
                                   all_block=','.join(all_list))


def _create_backlog_py(space_list: List[str]) -> str:
    objects = ', '.join([o.title() for o in space_list])
    return BACKLOG_TEMPLATE.format(objects=objects)


def _write_code(code: str, base_path: str, file_name: str) -> None:
    file_path = os.path.join(base_path, file_name)
    logger.info(f'write {file_path}')
    fixed_init_py = fix_code(code,
                             options=parse_args(['--aggressive', '']))

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
    for bs in bs_generator:
        try:
            api = APIGenerator(bs)
            if api.space_name not in stock:
                stock[api.space_name] = {}
                stock[api.space_name]['class'] = api.create_api_class()
                stock[api.space_name]['method'] = []
            stock[api.space_name]['method'].append(api.create_api_method())

        except Exception as e:
            logger.error(str(e))
            import sys
            sys.exit(1)

    _create_dir(api_path)

    for space, api_dict in stock.items():
        method_code = api_dict['class'] + ''.join(api_dict['method'])
        _write_code(method_code, api_path, f'{space}.py')

    init_py = _create_init_py(list(stock.keys()))
    _write_code(init_py, api_path, '__init__.py')

    backlog_py = _create_backlog_py(list(stock.keys()))
    _write_code(backlog_py, output_dir, 'backlog.py')


def create_api_from_file(data_dir: str = DATA_DIR) -> None:
    bs_generator = _get_bs_from_file(data_dir)
    _create_api_from_bs_generator(bs_generator)


def crete_api_from_web(download_wait_time: int = DOWNLOAD_WAIT_TIME) -> None:
    bs_generator = _get_bs_from_web(download_wait_time)
    _create_api_from_bs_generator(bs_generator)


def download_doc_file(data_dir: str,
                      download_wait_time: int = DOWNLOAD_WAIT_TIME) -> None:
    _create_dir(data_dir)
    for api_url in _get_api_urls():
        r = requests.get(api_url)
        time.sleep(download_wait_time)
        file_name = api_url.split('/')[-1]
        logger.info('write file: {sleep}')
        with open(os.path.join(data_dir, file_name + '.html'), 'wb') as f:
            f.write(r.content)


class APIGenerator:
    _under_scorer1 = re.compile(r'(.)([A-Z][a-z]+)')
    _under_scorer2 = re.compile('([a-z0-9])([A-Z])')

    def __init__(self, bs: BeautifulSoup) -> None:
        self.bs = bs
        self._method_type = ''
        self._api_path = ''
        self._url_parameters: Parameters = []
        self._form_parameters: Parameters = []
        self._query_parameters: Parameters = []
        self._short_path = ''
        self._space_name = ''
        self._api_name = ''
        self._api_description = ''

    @classmethod
    def camel_to_snake(cls, string: str) -> str:
        subbed = cls._under_scorer1.sub(r'\1_\2', string)
        return cls._under_scorer2.sub(r'\1_\2', subbed).lower()

    @classmethod
    def convert_to_correct_name(cls, string: str) -> str:
        if string == 'id':
            string = '_id'
        return cls.camel_to_snake(string)

    @property
    def api_name(self) -> str:
        if self._api_name:
            return self._api_name
        raw_api_name = self.bs.find('h2')['id']
        self._api_name = raw_api_name.replace('-', '_')
        return self._api_name

    @property
    def api_description(self) -> str:
        if self._api_description:
            return self._api_description
        api_name_element = self.bs.find('h2')
        for element in api_name_element.next_elements:
            if element.name == 'p':
                self._api_description = element.contents[0].replace('\n', ' ')
                return self._api_description
        raise Exception('Not Found Description')

    @property
    def method_type(self) -> str:
        if self._method_type:
            return self._method_type
        for api_path in self.bs.find_all('h3', id='method'):
            for element in api_path.next_elements:
                if element.name == 'code':
                    self._method_type = element.contents[0].replace(' \n', '')
                    return self._method_type
        raise Exception('Not Found Method')

    @property
    def api_path(self) -> str:
        if self._api_path:
            return self._api_path
        for api_path in self.bs.find_all('h3', id='url'):
            for element in api_path.next_elements:
                if element.name == 'code':
                    self._api_path = element.contents[0].replace(' \n', '')
                    return self._api_path
        raise Exception('Not Found API Path')

    @property
    def short_path(self) -> str:
        if self._short_path:
            return self._short_path
        self._short_path = self.api_path.replace(API_ROOT, '')
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
        self._url_parameters = self._get_parameters('url-parameters')
        return self._url_parameters

    def _get_parameters(self, html_id: str) -> Parameters:
        for parameters in self.bs.find_all('h3', id=html_id):
            for element in parameters.next_elements:
                if element.name == 'tbody':
                    tbody: Tag = element
                    lines = tbody.find_all('tr')
                    return [[td.contents[0]
                             for td in line.find_all('td') if td.contents]
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

    def create_api_call_args(self) -> str:
        api_call_args = []

        if self.url_parameters:
            path = re.sub(':.[^/]+', '{}', self.short_path)
            parameter_names = [self.convert_to_correct_name(url_parameter[0])
                               for
                               url_parameter in
                               self.url_parameters]
            parameter_args = ', '.join(parameter_names)
            api_call_args.append(f'\'{path}\'.format({parameter_args})')
        else:
            api_call_args.append(f'\'{self.short_path}\'')

        api_call_args.append(f'method=\'{self.method_type}\'')

        if self.query_parameters:
            api_call_args.append('query_parameters=query_parameters')

        if self.form_parameters:
            api_call_args.append('form_parameters=form_parameters')

        return ', '.join(api_call_args)

    def create_method_args(self) -> str:
        method_args = []

        for url_parameter in self.url_parameters:
            parameter_name = url_parameter[0]
            method_args.append(self.convert_to_correct_name(parameter_name))

        if self.query_parameters:
            method_args.append('query_parameters')

        if self.form_parameters:
            method_args.append('form_parameters')

        arg_string = ', '.join(method_args)
        if arg_string:
            return f', {arg_string}'
        else:
            return ''

    def create_args_doc(self) -> str:
        def get_arg_doc(name: str, description: str, _type: str) -> str:
            return f':param {_type} {name}: {description}'

        newline_and_indent: str = '\n        '
        args_doc = []

        for url_parameter in self.url_parameters:
            parameter_name = self.convert_to_correct_name(url_parameter[0])
            parameter_raw_type = url_parameter[1]
            if parameter_raw_type == 'Number':
                parameter_type = 'int'
            else:
                parameter_type = 'str'
            if len(url_parameter) > 2:
                parameter_description = url_parameter[2]
            else:
                parameter_description = parameter_name

            args_doc.append((parameter_name, parameter_description,
                             parameter_type))

        if self.query_parameters:
            args_doc.append(
                ('query_parameters', 'query_parameters', 'dict'))

        if self.form_parameters:
            args_doc.append(
                ('form_parameters', 'form_parameters', 'dict'))

        if args_doc:
            args_doc_str = [get_arg_doc(*a) for a in args_doc]
            return newline_and_indent + newline_and_indent.join(args_doc_str) \
                   + newline_and_indent
        else:
            return ''

    def create_method_doc(self) -> str:
        newline_and_indent: str = '\n        '
        return newline_and_indent + self.api_description + newline_and_indent

    def create_api_class(self) -> str:
        return API_CLASS_TEMPLATE.format(
            space_name=self.space_name.title()
        )

    def create_api_method(self) -> str:
        return API_METHOD_TEMPLATE.format(
            method_args=self.create_method_args(),
            args_doc=self.create_args_doc(),
            method_doc=self.create_method_doc(),
            api_name=self.api_name,
            api_call_args=self.create_api_call_args())


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
                                            help='download backlog document html')
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
