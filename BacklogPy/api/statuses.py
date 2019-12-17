# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from deprecated import deprecated

from BacklogPy.base import BacklogBase


class Statuses(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Statuses, self).__init__(space_id, api_key)

    @deprecated(reason="This API has been deprecated and is no longer recommended for use. Please replace it with Get Status List of Project.https://developer.nulab.com/docs/backlog/api/2/get-status-list-of-project/")
    def get_status_list(self):
        """
        Returns list of statuses. ※ Deprecated API. https://developer.nulab.com/docs/backlog/api/2/get-status-list-of-project/

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/statuses', method='GET')
