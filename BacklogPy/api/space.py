# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Space(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Space, self).__init__(space_id, api_key)

    def get_recent_updates(self, query_parameters):
        """
        Returns recent updates in your space.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/space/activities', method='GET',
                             query_parameters=query_parameters)

    def get_space_disk_usage(self):
        """
        Returns information about space disk usage.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/space/diskUsage', method='GET')

    def get_space_logo(self):
        """
        Returns logo image of your space.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/space/image', method='GET')

    def get_space_notification(self):
        """
        Returns space notification.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/space/notification', method='GET')

    def get_space(self):
        """
        Returns information about your space.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/space', method='GET')

    def post_attachment_file(self):
        """
        Posts an attachment file for issue or wiki. Returns id of the attachment file.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/space/attachment', method='POST')

    def update_space_notification(self):
        """
        Updates space notification.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/space/notification', method='PUT')
