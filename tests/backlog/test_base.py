from __future__ import absolute_import

import six

if six.PY3:
    from unittest import TestCase, mock
else:
    import sys

    if sys.version_info < (2, 7, 0):
        from unittest2 import TestCase
    else:
        from unittest import TestCase
    import mock

from BacklogPy.base import BacklogBase


class TestBacklogBase(TestCase):
    def test_api_url(self):
        backlog_base = BacklogBase('space-id', 'api-key')
        self.assertEqual(backlog_base._api_url,
                         'https://space-id.backlog.jp/api/v2')

    def test_request(self):
        with mock.patch('requests.request') as m:
            backlog_base = BacklogBase('space-id', 'api-key')
            backlog_base._request('/path')
            args, kwargs = m.call_args_list[0]
            self.assertTupleEqual(args, ('GET',
                                         'https://space-id.backlog.jp/api/v2/path'))
            self.assertDictEqual(kwargs,
                                 {'params': {'apiKey': 'api-key'}, 'data': {},
                                  'headers': {}})

        with mock.patch('requests.request') as m:
            backlog_base._request('/path', method='POST')
            args, kwargs = m.call_args_list[0]
            self.assertTupleEqual(args,
                                  ('POST',
                                   'https://space-id.backlog.jp/api/v2/path'))
            self.assertDictEqual(kwargs,
                                 {'params': {'apiKey': 'api-key'}, 'data': {},
                                  'headers': {}})

        with mock.patch('requests.request') as m:
            backlog_base._request('/path', method='POST',
                                  query_parameters={'id': 123})
            args, kwargs = m.call_args_list[0]
            self.assertTupleEqual(args,
                                  ('POST',
                                   'https://space-id.backlog.jp/api/v2/path'))
            self.assertDictEqual(kwargs,
                                 {'params': {'apiKey': 'api-key', 'id': 123},
                                  'data': {},
                                  'headers': {}})

        with mock.patch('requests.request') as m:
            backlog_base._request('/path', method='POST',
                                  query_parameters={'id': 123},
                                  form_parameters={'name': 'abc'})
            args, kwargs = m.call_args_list[0]
            self.assertTupleEqual(args,
                                  ('POST',
                                   'https://space-id.backlog.jp/api/v2/path'))
            self.assertDictEqual(kwargs,
                                 {'params': {'apiKey': 'api-key', 'id': 123},
                                  'data': {'name': 'abc'},
                                  'headers': {
                                      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}})
