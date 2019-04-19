import os
import uuid
from tempfile import NamedTemporaryFile, TemporaryDirectory, gettempdir
from typing import List
from unittest import TestCase, mock

from bs4 import BeautifulSoup

from api_generator import api_generator


def get_bs(content: str):
    return BeautifulSoup(content, 'lxml')


class MockResponse:
    def __init__(self, content: str):
        self.content = content


class TestHTMLDownload(TestCase):
    @mock.patch('requests.get')
    def test_get_bs_from_url(self, requests_mock):
        html = '<html><body><a>hello</a></body></html>'

        requests_mock.return_value = MockResponse(html)
        bs = api_generator._get_bs_from_url('http://localhost/path')
        args, kwargs = requests_mock.call_args_list[0]
        self.assertTupleEqual(args, ('http://localhost/path',))
        expect_bs = get_bs(html)
        self.assertEqual(bs, expect_bs)

    @mock.patch('requests.get')
    def test_get_api_urls(self, requests_mock):
        html = '<html><body><optgroup label="Backlog API">' \
               '<option value="/path1"></option>' \
               '<option value="/path2"></option>' \
               '<option value="/path3"></option>' \
               '</optgroup></body></html>'

        developer_url = 'http://localhost/developer'
        requests_mock.return_value = MockResponse(html)
        urls = api_generator._get_api_urls(developer_url=developer_url,
                                           overview_url='http://localhost/overview')

        expect_list = [developer_url + '/path1',
                       developer_url + '/path2',
                       developer_url + '/path3']

        self.assertListEqual(list(urls), expect_list)

    def test_get_bs_from_file(self):
        unknown_directory_path = os.path.join(gettempdir(), str(uuid.uuid4()))
        bss = api_generator._get_bs_from_file(unknown_directory_path)
        with self.assertRaises(Exception):
            next(bss)

        html = '<html><body><a>hello</a></body></html>'

        with TemporaryDirectory() as html_directory:
            with NamedTemporaryFile(dir=html_directory, mode='w+') as f:
                f.write(html)
                f.flush()
                bs_list = list(api_generator._get_bs_from_file(html_directory))
        self.assertEqual(bs_list[0], get_bs(html))

    @mock.patch('api_generator.api_generator._get_api_urls')
    @mock.patch('api_generator.api_generator._get_bs_from_url')
    def test_bs_from_web(self, get_bs_from_url_mock, get_api_urls_mock):
        get_api_urls_mock.return_value = ['url1', 'url2', 'url3']
        html_list = ['<html><body><p>url1</p></body></html>',
                     '<html><body><p>url2</p></body></html>',
                     '<html><body><p>url3</p></body></html>']

        bs_list = [get_bs(html) for html in html_list]

        def get_bs_from_url_mock_function(url):
            html = f'<html><body><p>{url}</p></body></html>'
            return get_bs(html)

        get_bs_from_url_mock.side_effect = get_bs_from_url_mock_function
        bss = api_generator._get_bs_from_web()

        self.assertListEqual(list(bss), bs_list)

    @mock.patch('requests.get')
    @mock.patch('api_generator.api_generator._get_api_urls')
    def test_download_doc_file(self, get_api_urls_mock,
                               requests_mock) -> None:
        class MockMultiResponse:
            def __init__(self, contents: List[bytes]):
                self._contents = contents
                self._gen = (content for content in self._contents)

            @property
            def content(self) -> bytes:
                return next(self._gen)

        html_list = [b'<html><body>1</body></html>',
                     b'<html><body>1</body></html>',
                     b'<html><body>1</body></html>']

        requests_mock.return_value = MockMultiResponse(html_list)
        get_api_urls_mock.return_value = ['/api/path/1', '/api/path/2',
                                          '/api/path/3']
        with TemporaryDirectory() as target_directory:
            api_generator.download_doc_file(target_directory, 0)

            with open(os.path.join(target_directory, '1.html'), 'rb') as f:
                self.assertEqual(f.read(), html_list[0])

            with open(os.path.join(target_directory, '2.html'), 'rb') as f:
                self.assertEqual(f.read(), html_list[1])

            with open(os.path.join(target_directory, '3.html'), 'rb') as f:
                self.assertEqual(f.read(), html_list[2])


class TestCreatePyFile(TestCase):
    def test_create_init_py(self):
        init_py = api_generator._create_init_py(['space1', 'space2', 'space3'])
        expect_init_py = '''# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from BacklogPy.api.space1 import Space1
from BacklogPy.api.space2 import Space2
from BacklogPy.api.space3 import Space3

__all__ = ['Space1','Space2','Space3']

'''

        self.assertEqual(init_py, expect_init_py)

    def test_create_backlog_py(self):
        backlog_py = api_generator._create_backlog_py(
            ['space1', 'space2', 'space3'])

        expect_backlog_py = '''# coding: utf-8
    
"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.api import *


class Backlog(Space1, Space2, Space3):
    pass
'''

        self.assertEqual(backlog_py, expect_backlog_py)

    def test_write_code(self):
        code = '''def   hello(  ):
          print(  'hello','abc')'''

        expect_code = '''def hello():
    print('hello', 'abc')\n'''
        with TemporaryDirectory() as output_directory:
            with NamedTemporaryFile(dir=output_directory, mode='w+') as f:
                api_generator._write_code(code, output_directory, f.name)
                f.seek(0)
                self.assertEqual(f.read(), expect_code)

    def test_create_dir(self):
        with TemporaryDirectory() as target_directory:
            self.assertEqual(api_generator._create_dir(target_directory), None)
        with NamedTemporaryFile() as target_file:
            with self.assertRaises(Exception):
                api_generator._create_dir(target_file.name)

        target_directory = os.path.join(gettempdir(), str(uuid.uuid4()))
        try:
            api_generator._create_dir(target_directory)
            self.assertEqual(os.path.isdir(target_directory), True)
        finally:
            os.rmdir(target_directory)

    def test_create_api_from_bs_generator(self):
        html_template = '<html><body>' \
                        '<h2 id="test_api_name"><p>hello{num}</p></h2></body>' \
                        '<h3 id="url"><code>/api/v2/hello</code></h3>' \
                        '<h3 id="method"><code>hello</code></h3>' \
                        '<h3 id="url-parameters">' \
                        '<tbody><tr><td>hello</td><td>String</td></tr>' \
                        '<tr><td>bye</td><td>String</td></tr>' \
                        '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
                        '</tbody></h3>' \
                        '<h3 id="form-parameters">' \
                        '<tbody><tr><td>hello</td><td>String</td><</tr>' \
                        '<tr><td>bye</td><td>String</td></tr>' \
                        '</tbody></h3></body></html>'

        html_list = [html_template.format(num=i) for i in range(2)]
        bs_generator = (get_bs(html) for html in html_list)
        expect_hello_class = '''# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Hello(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Hello, self).__init__(space_id, api_key)

    def test_api_name_raw(self, hello, bye, num, form_parameters):
        """
        hello0

        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/hello'.format(hello, bye, num),
                             method='hello', form_parameters=form_parameters)

    def test_api_name(self, hello, bye, num, hello=None, bye=None):
        """
        hello0

        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param str hello: hello
        :param str bye: bye

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'hello': hello,
            'bye': bye
        }

        return self._request('/hello'.format(hello, bye, num),
                             method='hello', form_parameters=form_parameters)

    def test_api_name_raw(self, hello, bye, num, form_parameters):
        """
        hello1

        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/hello'.format(hello, bye, num),
                             method='hello', form_parameters=form_parameters)

    def test_api_name(self, hello, bye, num, hello=None, bye=None):
        """
        hello1

        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param str hello: hello
        :param str bye: bye

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'hello': hello,
            'bye': bye
        }

        return self._request('/hello'.format(hello, bye, num),
                             method='hello', form_parameters=form_parameters)
'''
        expect_init = '''# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from BacklogPy.api.hello import Hello

__all__ = ['Hello']
'''

        expect_backlog_py = '''# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.api import *


class Backlog(Hello):
    pass
'''

        with TemporaryDirectory() as target_directory:
            api_generator._create_api_from_bs_generator(bs_generator,
                                                        target_directory)
            with open(os.path.join(target_directory, 'api/hello.py')) as f:
                self.assertEqual(f.read(), expect_hello_class)

            with open(os.path.join(target_directory, 'api/__init__.py')) as f:
                self.assertEqual(f.read(), expect_init)

            with open(os.path.join(target_directory, 'backlog.py')) as f:
                self.assertEqual(f.read(), expect_backlog_py)

        html_template = '<html><body>' \
                        '<h2 id="test_api_name"><p>hello{num} ※ Deprecated API. xxx <a href="https://backlogpy.org"></a></p></h2></body>' \
                        '<h3 id="url"><code>/api/v2/hello</code></h3>' \
                        '<h3 id="method"><code>hello</code></h3>' \
                        '<h3 id="url-parameters">' \
                        '<tbody><tr><td>hello</td><td>String</td></tr>' \
                        '<tr><td>bye</td><td>String</td></tr>' \
                        '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
                        '</tbody></h3>' \
                        '<h3 id="form-parameters">' \
                        '<tbody><tr><td>hello</td><td>String</td><</tr>' \
                        '<tr><td>bye</td><td>String</td></tr>' \
                        '</tbody></h3></body></html>'

        html_list = [html_template.format(num=i) for i in range(2)]
        bs_generator = (get_bs(html) for html in html_list)
        expect_hello_class = '''# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from deprecated import deprecated

from BacklogPy.base import BacklogBase


class Hello(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Hello, self).__init__(space_id, api_key)

    @deprecated(reason="xxx https://backlogpy.org")
    def test_api_name_raw(self, hello, bye, num, form_parameters):
        """
        hello0 ※ Deprecated API. xxx https://backlogpy.org

        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/hello'.format(hello, bye, num),
                             method='hello', form_parameters=form_parameters)

    @deprecated(reason="xxx https://backlogpy.org")
    def test_api_name(self, hello, bye, num, hello=None, bye=None):
        """
        hello0 ※ Deprecated API. xxx https://backlogpy.org

        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param str hello: hello
        :param str bye: bye

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'hello': hello,
            'bye': bye
        }

        return self._request('/hello'.format(hello, bye, num),
                             method='hello', form_parameters=form_parameters)

    @deprecated(reason="xxx https://backlogpy.org")
    def test_api_name_raw(self, hello, bye, num, form_parameters):
        """
        hello1 ※ Deprecated API. xxx https://backlogpy.org

        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/hello'.format(hello, bye, num),
                             method='hello', form_parameters=form_parameters)

    @deprecated(reason="xxx https://backlogpy.org")
    def test_api_name(self, hello, bye, num, hello=None, bye=None):
        """
        hello1 ※ Deprecated API. xxx https://backlogpy.org

        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param str hello: hello
        :param str bye: bye

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'hello': hello,
            'bye': bye
        }

        return self._request('/hello'.format(hello, bye, num),
                             method='hello', form_parameters=form_parameters)
'''

        with TemporaryDirectory() as target_directory:
            api_generator._create_api_from_bs_generator(bs_generator,
                                                        target_directory)
            with open(os.path.join(target_directory, 'api/hello.py')) as f:
                self.assertEqual(f.read(), expect_hello_class)


class TestParameter(TestCase):
    def test_camel_to_snake(self):
        camel_case = 'TestCase'
        other_case = 'testCase'
        expect_snake_case = 'test_case'
        self.assertEqual(api_generator.Parameter.camel_to_snake(camel_case),
                         expect_snake_case)
        self.assertEqual(api_generator.Parameter.camel_to_snake(other_case),
                         expect_snake_case)

    def test_convert_to_correct_name(self):
        camel_case = 'TestCase'
        other_case = 'id'
        expect_snake_case = 'test_case'
        expect_id = '_id'
        self.assertEqual(
            api_generator.Parameter.convert_to_correct_name(camel_case),
            expect_snake_case)
        self.assertEqual(
            api_generator.Parameter.convert_to_correct_name(other_case),
            expect_id)

    def test_parameter_doc(self):
        parameter_str = api_generator.Parameter('string', 'String')
        self.assertEqual(parameter_str.doc, ':param str string: string')

        parameter_int = api_generator.Parameter('number', 'Number')
        self.assertEqual(parameter_int.doc, ':param int number: number')

        parameter_bool = api_generator.Parameter('boolean', 'Boolean')
        self.assertEqual(parameter_bool.doc, ':param bool boolean: boolean')

        parameter_dict = api_generator.Parameter('dict', 'dict')
        self.assertEqual(parameter_dict.doc, ':param dict dict: dict')

        parameter_str_list = api_generator.Parameter('string[]', 'String')
        self.assertEqual(parameter_str_list.doc,
                         ':param list[str] or str string: string[]')

        parameter_str_list = api_generator.Parameter('number[]', 'Number')
        self.assertEqual(parameter_str_list.doc,
                         ':param list[int] or int number: number[]')

    def test___lt__(self):
        parameter_str_1 = api_generator.Parameter('abc', 'String')
        parameter_str_2 = api_generator.Parameter('bcd', 'String')
        self.assertTrue(parameter_str_1 < parameter_str_2)

        parameter_str_3 = api_generator.Parameter('2', 'String')
        parameter_str_4 = api_generator.Parameter('1', 'String')
        self.assertTrue(parameter_str_4 < parameter_str_3)


class TestAPIGenerator(TestCase):
    def test_api_name(self):
        html = '<html><body><h2 id="test_api_name" >hello</h2></body></html>'

        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.api_name, 'test_api_name')
        self.assertEqual(api.api_name, 'test_api_name')

    def test_api_description(self):
        html = '<html><body><h2><p>hello</p></h2></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.api_description, 'hello')
        self.assertEqual(api.api_description, 'hello')
        self.assertFalse(api.deprecated)
        self.assertEqual(api.modules, set())

        html = '<html><body><h2><span>hello<span/></h2></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        with self.assertRaises(Exception):
            _ = api.api_description

        html = '<html><body><h2><p>hello ※ Deprecated API. xxx <a href="https://backlogpy.org"></a></p></h2></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.api_description, 'hello ※ Deprecated API. xxx https://backlogpy.org')
        self.assertTrue(api.deprecated)
        self.assertEqual(api.modules, {'from deprecated import deprecated'})

    def test_method_type(self):
        html = '<html><body><h3 id="method"><code>hello</code></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.method_type, 'hello')
        self.assertEqual(api.method_type, 'hello')

        html = '<html><body><h3><p>hello</p></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        with self.assertRaises(Exception):
            _ = api.method_type

    def test_api_path(self):
        html = '<html><body><h3 id="url"><code>/api/v2/hello</code></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.api_path, '/api/v2/hello')
        self.assertEqual(api.api_path, '/api/v2/hello')

        html = '<html><body><h3><p>hello</p></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        with self.assertRaises(Exception):
            _ = api.api_path

    def test_short_path(self):
        html = '<html><body><h3 id="url"><code>/api/v2/hello</code></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.short_path, '/hello')
        self.assertEqual(api.short_path, '/hello')

    def test_space_name(self):
        html = '<html><body><h3 id="url"><code>/api/v2/hello</code></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.space_name, 'hello')
        self.assertEqual(api.space_name, 'hello')

    def test_get_parameters(self):
        html = '<html><body><h3 id="param">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr></tbody></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        parameters = api._get_parameters('param')
        self.assertEqual(parameters[0].name, 'hello')
        self.assertEqual(parameters[0].type.doc, 'str')
        self.assertEqual(parameters[1].name, 'bye')
        self.assertEqual(parameters[1].type.doc, 'str')

        html = '<html><body></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.url_parameters,
                         [])

    def test_url_parameters(self):
        html = '<html><body><h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.url_parameters[0].name, 'hello')
        self.assertEqual(api.url_parameters[0].type.doc, 'str')
        self.assertEqual(api.url_parameters[1].name, 'bye')
        self.assertEqual(api.url_parameters[1].type.doc, 'str')

    def test_form_parameters(self):
        html = '<html><body><h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.form_parameters[0].name, 'hello')
        self.assertEqual(api.form_parameters[0].type.doc, 'str')
        self.assertEqual(api.form_parameters[1].name, 'bye')
        self.assertEqual(api.form_parameters[1].type.doc, 'str')

    def test_query_parameters(self):
        html = '<html><body><h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.query_parameters[0].name, 'hello')
        self.assertEqual(api.query_parameters[0].type.doc, 'str')
        self.assertEqual(api.query_parameters[1].name, 'bye')
        self.assertEqual(api.query_parameters[1].type.doc, 'str')

    def test_has_strict_method(self):
        html = '<html><body></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertFalse(api.has_strict_method)

        html = '<html><body><h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertTrue(api.has_strict_method)

        html = '<html><body><h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertTrue(api.has_strict_method)

        html = '<html><body><h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        api = api_generator.APIGenerator(get_bs(html))
        self.assertTrue(api.has_strict_method)

    def test_create_api_call_args(self):
        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        expect_api_call_args = "'/hello'.format(hello, bye), method='hello'," \
                               " query_parameters=query_parameters," \
                               " form_parameters=form_parameters"
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_api_call_args(), expect_api_call_args)

        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '</h3></body></html>'
        expect_api_call_args = "'/hello', method='hello'"
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_api_call_args(), expect_api_call_args)

    def test_create_method_args(self):
        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        expect_create_method_args = ", hello, bye, query_parameters, form_parameters"
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_method_args(), expect_create_method_args)

        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        expect_create_method_args = ", hello, bye, hello=None, bye=None," \
                                    " hello=None, bye=None"
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_method_args(strict=True),
                         expect_create_method_args)

        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>goodbye (Required)</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        expect_create_method_args = ", hello, bye, goodbye, hello=None," \
                                    " hello=None, bye=None"
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_method_args(strict=True),
                         expect_create_method_args)

        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '</tbody></h3></body></html>'
        expect_create_method_args = ""
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_method_args(),
                         expect_create_method_args)

    def test_create_args_doc(self):
        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        expect_args_doc = '''\n        :param str hello: hello
        :param str bye: bye
        :param dict query_parameters: query_parameters
        :param dict form_parameters: form_parameters\n        '''
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_args_doc(),
                         expect_args_doc)

        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'
        expect_args_doc = '''\n        :param str hello: hello
        :param str bye: bye
        :param str hello: hello
        :param str bye: bye
        :param str hello: hello
        :param str bye: bye\n        '''
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_args_doc(strict=True),
                         expect_args_doc)
        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '</tbody></h3></body></html>'
        expect_args_doc = ""
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_args_doc(),
                         expect_args_doc)

        html = '<html><body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td></tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
               '</tbody></h3></body></html>'
        expect_args_doc = '''\n        :param str hello: hello
        :param str bye: bye
        :param int num: description\n        '''
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_args_doc(),
                         expect_args_doc)

    def test_create_parameter_assignment(self):
        html = '<html><body>' \
               '<h2><p>hello</p></h2></body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="form-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td><</tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '</tbody></h3></body></html>'

        expect_parameter_assignment = '''query_parameters = {
        'hello': hello,
            'bye': bye
        }

form_parameters = {
        'hello': hello,
            'bye': bye
        }'''
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_parameter_assignment(),
                         expect_parameter_assignment)

    def test_create_method_doc(self):
        html = '<html><body>' \
               '<h2><p>hello</p></h2></body>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="url-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td></tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
               '</tbody></h3></body></html>'
        expect_method_doc = '''
        hello
        '''
        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api._create_method_doc(),
                         expect_method_doc)

    def test_create_api_class(self):
        html = '<html><body><h3 id="url"><code>/api/v2/hello</code></h3></body></html>'
        expect_api_class = '''# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import
{module_import}
from BacklogPy.base import BacklogBase


class Hello(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Hello, self).__init__(space_id, api_key)
'''
        api = api_generator.APIGenerator(get_bs(html))
        print(f'"{api.create_api_class()}"')
        self.assertEqual(api.create_api_class(),
                         expect_api_class)

    def test_create_api_method(self):
        html = '<html><body>' \
               '<h2 id="test_api_name" >hello</h2>' \
               '<html><body><h2><p>hello</p></h2></body></html>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td></tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
               '<tr><td>boolean</td><td>Boolean</td></tr>' \
               '</tbody></h3></body></html>'

        expect_api_method = '''
    def test_api_name_raw(self, query_parameters):
        """
        hello
        
        :param dict query_parameters: query_parameters
        
        :return:  requests Response object 
        :rtype: requests.Response
        """
        
        
        
        return self._request('/hello', method='hello', query_parameters=query_parameters)
'''

        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.create_api_method(),
                         expect_api_method)

        expect_api_method = '''
    def test_api_name(self, hello=None, bye=None, num=None, boolean=None):
        """
        hello
        
        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param bool boolean: boolean
        
        :return:  requests Response object 
        :rtype: requests.Response
        """
        
        query_parameters = {
        'hello': hello,
            'bye': bye,
            'num': num,
            'boolean': self._bool_to_str(boolean)
        }
        
        return self._request('/hello', method='hello', query_parameters=query_parameters)
'''

        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.create_api_method(strict=True),
                         expect_api_method)

        html = '<html><body>' \
               '<h2 id="test_api_name" >hello</h2>' \
               '<html><body><h2><p>hello ※ Deprecated API. xxx <a href="https://backlogpy.org"></a></p></h2></html>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="query-parameters">' \
               '<tbody><tr><td>hello</td><td>String</td></tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
               '<tr><td>boolean</td><td>Boolean</td></tr>' \
               '</tbody></h3></body></html>'

        expect_api_method = '''
    @deprecated(reason="xxx https://backlogpy.org")
    def test_api_name_raw(self, query_parameters):
        """
        hello ※ Deprecated API. xxx https://backlogpy.org
        
        :param dict query_parameters: query_parameters
        
        :return:  requests Response object 
        :rtype: requests.Response
        """
        
        
        
        return self._request('/hello', method='hello', query_parameters=query_parameters)
'''

        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.create_api_method(),
                         expect_api_method)

    def test_create_api_method_with_broken_header(self):
        html = '<html><body>' \
               '<h2 id="test_api_name" >hello</h2>' \
               '<html><body><h2><p>hello</p></h2></body></html>' \
               '<h3 id="url"><code>/api/v2/hello</code></h3>' \
               '<h3 id="method"><code>hello</code></h3>' \
               '<h3 id="query-parameters">' \
               '<thead><tr><th>header_hello</th><th>String</th><th>header description</th><tr></thead>' \
               '<tbody><tr><td>hello</td><td>String</td></tr>' \
               '<tr><td>bye</td><td>String</td></tr>' \
               '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
               '<tr><td>boolean</td><td>Boolean</td></tr>' \
               '</tbody></h3></body></html>'

        expect_api_method = '''
    def test_api_name_raw(self, query_parameters):
        """
        hello
        
        :param dict query_parameters: query_parameters
        
        :return:  requests Response object 
        :rtype: requests.Response
        """
        
        
        
        return self._request('/hello', method='hello', query_parameters=query_parameters)
'''

        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.create_api_method(),
                         expect_api_method)

        expect_api_method = '''
    def test_api_name(self, header_hello=None, hello=None, bye=None, num=None, boolean=None):
        """
        hello
        
        :param str header_hello: header description
        :param str hello: hello
        :param str bye: bye
        :param int num: description
        :param bool boolean: boolean
        
        :return:  requests Response object 
        :rtype: requests.Response
        """
        
        query_parameters = {
        'header_hello': header_hello,
            'hello': hello,
            'bye': bye,
            'num': num,
            'boolean': self._bool_to_str(boolean)
        }
        
        return self._request('/hello', method='hello', query_parameters=query_parameters)
'''

        api = api_generator.APIGenerator(get_bs(html))
        self.assertEqual(api.create_api_method(strict=True),
                         expect_api_method)

    def test___lt__(self):
        html_1 = '<html><body>' \
                 '<h2 id="test_api_name_abc" >hello</h2>' \
                 '<html><body><h2><p>hello</p></h2></body></html>' \
                 '<h3 id="url"><code>/api/v2/hello</code></h3>' \
                 '<h3 id="method"><code>hello</code></h3>' \
                 '<h3 id="query-parameters">' \
                 '<tbody><tr><td>hello</td><td>String</td></tr>' \
                 '<tr><td>bye</td><td>String</td></tr>' \
                 '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
                 '<tr><td>boolean</td><td>Boolean</td></tr>' \
                 '</tbody></h3></body></html>'

        html_2 = '<html><body>' \
                 '<h2 id="test_api_name_bcd" >hello</h2>' \
                 '<html><body><h2><p>hello</p></h2></body></html>' \
                 '<h3 id="url"><code>/api/v2/hello</code></h3>' \
                 '<h3 id="method"><code>hello</code></h3>' \
                 '<h3 id="query-parameters">' \
                 '<tbody><tr><td>hello</td><td>String</td></tr>' \
                 '<tr><td>bye</td><td>String</td></tr>' \
                 '<tr><td>num</td><td>Number</td><td>description</td></tr>' \
                 '<tr><td>boolean</td><td>Boolean</td></tr>' \
                 '</tbody></h3></body></html>'

        api_1 = api_generator.APIGenerator(get_bs(html_1))
        api_2 = api_generator.APIGenerator(get_bs(html_2))
        self.assertTrue(api_1 < api_2)
