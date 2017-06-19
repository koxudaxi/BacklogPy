# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Watchings(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Watchings, self).__init__(space_id, api_key)

    def add_watching(self, form_parameters):
        """
        Adds a watching. User can add a own watching.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/watchings', method='POST',
                             form_parameters=form_parameters)

    def delete_watching(self, watching_id):
        """
        Deletes a own watching. User can delete a own watching.

        :param int watching_id: watching ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/watchings/{}'.format(watching_id), method='DELETE')

    def get_watching(self, watching_id):
        """
        Returns the information about a watching.

        :param int watching_id: Watching ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/watchings/{}'.format(watching_id), method='GET')

    def mark_watching_as_read(self, watching_id):
        """
        Mark a watching as read.

        :param int watching_id: watching ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/watchings/{}/markAsRead'.format(watching_id), method='POST')

    def update_watching(self, watching_id, form_parameters):
        """
        Updates a watching. User can update own note.

        :param int watching_id: watching ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/watchings/{}'.format(watching_id),
                             method='PATCH', form_parameters=form_parameters)
