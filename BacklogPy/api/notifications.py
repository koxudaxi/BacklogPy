# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Notifications(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Notifications, self).__init__(space_id, api_key)

    def count_notification_raw(self, query_parameters):
        """
        Returns number of Notifications.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/notifications/count',
            method='GET',
            query_parameters=query_parameters)

    def count_notification(
            self,
            resource_already_read=None,
            already_read=None):
        """
        Returns number of Notifications.

        :param bool resource_already_read: This parameter is optional. Set to false for unread notification count and true for already read notification count.
        :param bool already_read: This parameter is optional. Set this parameter to false to get unread notification count since the last time checked by user and true for already read notification count.

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'resourceAlreadyRead': self._bool_to_str(resource_already_read),
            'alreadyRead': self._bool_to_str(already_read)
        }

        return self._request(
            '/notifications/count',
            method='GET',
            query_parameters=query_parameters)

    def get_notification_raw(self, query_parameters):
        """
        Returns own notifications.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/notifications',
            method='GET',
            query_parameters=query_parameters)

    def get_notification(
            self,
            min_id=None,
            max_id=None,
            count=None,
            order=None,
            sender_id=None):
        """
        Returns own notifications.

        :param int min_id: minimum ID
        :param int max_id: maximum ID
        :param int count: number of records to retrieve(1-100) default=20
        :param str order: “asc” or “desc”
        :param int sender_id: sender ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'minId': min_id,
            'maxId': max_id,
            'count': count,
            'order': order,
            'senderId': sender_id
        }

        return self._request(
            '/notifications',
            method='GET',
            query_parameters=query_parameters)

    def read_notification(self, _id):
        """
        Changes notifications read.

        :param int _id: Notification ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/notifications/{}/markAsRead'.format(_id),
            method='POST')

    def reset_unread_notification_count(self):
        """
        Resets unread Notification count.

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/notifications/markAsRead', method='POST')
