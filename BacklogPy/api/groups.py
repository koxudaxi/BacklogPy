# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase, SUFFIX_JP


class Groups(BacklogBase):
    def __init__(self, space_id, api_key, suffix=SUFFIX_JP):
        super(Groups, self).__init__(space_id, api_key, suffix=suffix)

    def add_group_raw(self, form_parameters):
        """
        Adds new group. You can’t use this API at new plan space.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/groups',
            method='POST',
            form_parameters=form_parameters)

    def add_group(self, name, members=None):
        """
        Adds new group. You can’t use this API at new plan space.

        :param str name: Group Name
        :param list[int] or int members: User ID added to the group

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'members[]': members
        }

        return self._request(
            '/groups',
            method='POST',
            form_parameters=form_parameters)

    def delete_group(self, group_id):
        """
        Deletes group. You can’t use this API at new plan space.

        :param int group_id: Group ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/groups/{}'.format(group_id), method='DELETE')

    def get_group(self, group_id):
        """
        Returns information about group.

        :param int group_id: Group ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/groups/{}'.format(group_id), method='GET')

    def get_group_icon(self, group_id):
        """
        Downloads group icon.

        :param int group_id: group ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/groups/{}/icon'.format(group_id), method='GET')

    def get_list_of_groups_raw(self, query_parameters):
        """
        Returns list of groups.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/groups',
            method='GET',
            query_parameters=query_parameters)

    def get_list_of_groups(self, order=None, offset=None, count=None):
        """
        Returns list of groups.

        :param str order: “asc” or “desc” default=“desc”
        :param int offset: offset
        :param int count: number of records to retrieve(1-100) default=20

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'order': order,
            'offset': offset,
            'count': count
        }

        return self._request(
            '/groups',
            method='GET',
            query_parameters=query_parameters)

    def update_group_raw(self, group_id, form_parameters):
        """
        Updates information about group. You can’t use this API at new plan space.

        :param int group_id: Group ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/groups/{}'.format(group_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_group(self, group_id, name=None, members=None):
        """
        Updates information about group. You can’t use this API at new plan space.

        :param int group_id: Group ID
        :param str name: Group Name
        :param list[int] or int members: User ID added to the group

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'members[]': members
        }

        return self._request(
            '/groups/{}'.format(group_id),
            method='PATCH',
            form_parameters=form_parameters)
