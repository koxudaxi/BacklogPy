# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Groups(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Groups, self).__init__(space_id, api_key)

    def add_group(self, form_parameters):
        """
        Adds new group.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/groups', method='POST',
                             form_parameters=form_parameters)

    def delete_group(self, group_id):
        """
        Deletes group.

        :param int group_id: Group ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/groups/{}'.format(group_id), method='DELETE')

    def get_group(self, group_id):
        """
        Returns information about group.

        :param int group_id: Group ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/groups/{}'.format(group_id), method='GET')

    def get_list_of_groups(self, query_parameters):
        """
        Returns list of groups.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/groups', method='GET',
                             query_parameters=query_parameters)

    def update_group(self, group_id, form_parameters):
        """
        Updates information about group.

        :param int group_id: Group ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/groups/{}'.format(group_id),
                             method='PATCH', form_parameters=form_parameters)
