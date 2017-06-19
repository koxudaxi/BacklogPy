# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Priorities(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Priorities, self).__init__(space_id, api_key)

    def get_priority_list(self):
        """
        Returns list of priorities.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/priorities', method='GET')
