# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Statuses(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Statuses, self).__init__(space_id, api_key)

    def get_status_list(self):
        """
        Returns list of statuses.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/statuses', method='GET')
