# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Notifications(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Notifications, self).__init__(space_id, api_key)

    def count_notification(self, query_parameters):
        """
        Returns number of Notifications.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/notifications/count',
                             method='GET', query_parameters=query_parameters)

    def get_notification(self, query_parameters):
        """
        Returns own notifications.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/notifications', method='GET',
                             query_parameters=query_parameters)

    def read_notification(self, _id):
        """
        Changes notifications read.

        :param int _id: Notification ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/notifications/{}/markAsRead'.format(_id), method='POST')

    def reset_unread_notification_count(self):
        """
        Resets unread Notification count.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/notifications/markAsRead', method='POST')
