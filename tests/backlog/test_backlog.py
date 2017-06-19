from __future__ import absolute_import

from unittest import TestCase

from BacklogPy.backlog import *


class TestBacklog(TestCase):
    def test_create_instance(self):
        backlog_obj = Backlog('space-id', 'api-key')
        self.assertEqual(backlog_obj._api_url,
                         'https://space-id.backlog.jp/api/v2')

    def test_check_sub_class(self):
        self.assertTrue(issubclass(Backlog, Projects))
        self.assertTrue(issubclass(Backlog, Issues))
        self.assertTrue(issubclass(Backlog, Groups))
        self.assertTrue(issubclass(Backlog, Stars))
        self.assertTrue(issubclass(Backlog, Users))
        self.assertTrue(issubclass(Backlog, Watchings))
        self.assertTrue(issubclass(Backlog, Wikis))
        self.assertTrue(issubclass(Backlog, Notifications))
        self.assertTrue(issubclass(Backlog, Priorities))
        self.assertTrue(issubclass(Backlog, Space))
        self.assertTrue(issubclass(Backlog, Resolutions))
        self.assertTrue(issubclass(Backlog, Statuses))

