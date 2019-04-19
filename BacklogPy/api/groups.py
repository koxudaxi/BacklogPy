# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from deprecated import deprecated

from BacklogPy.base import BacklogBase


class Groups(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Groups, self).__init__(space_id, api_key)

    @deprecated(
        reason="Please replace it with Add Team .https://developer.nulab.com/docs/backlog/api/2/add-team/")
    def add_group_raw(self, form_parameters):
        """
        Adds new group. You can’t use this API at backlog.com space. ※ Deprecated API. Please replace it with Add Team .https://developer.nulab.com/docs/backlog/api/2/add-team/

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/groups',
            method='POST',
            form_parameters=form_parameters)

    @deprecated(
        reason="Please replace it with Add Team .https://developer.nulab.com/docs/backlog/api/2/add-team/")
    def add_group(self, name, members=None):
        """
        Adds new group. You can’t use this API at backlog.com space. ※ Deprecated API. Please replace it with Add Team .https://developer.nulab.com/docs/backlog/api/2/add-team/

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

    @deprecated(
        reason="Please replace it with Delete Team .https://developer.nulab.com/docs/backlog/api/2/delete-team/")
    def delete_group(self, group_id):
        """
        Deletes group. You can’t use this API at backlog.com space. ※ Deprecated API. Please replace it with Delete Team .https://developer.nulab.com/docs/backlog/api/2/delete-team/

        :param int group_id: Group ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/groups/{}'.format(group_id), method='DELETE')

    @deprecated(
        reason="Please replace it with Get Team .https://developer.nulab.com/docs/backlog/api/2/get-team/")
    def get_group(self, group_id):
        """
        Returns information about group. ※ Deprecated API. Please replace it with Get Team .https://developer.nulab.com/docs/backlog/api/2/get-team/

        :param int group_id: Group ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/groups/{}'.format(group_id), method='GET')

    @deprecated(
        reason="Please replace it with Get Team Icon .https://developer.nulab.com/docs/backlog/api/2/get-team-icon/")
    def get_group_icon(self, group_id):
        """
        Downloads group icon. ※ Deprecated API. Please replace it with Get Team Icon .https://developer.nulab.com/docs/backlog/api/2/get-team-icon/

        :param int group_id: group ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/groups/{}/icon'.format(group_id), method='GET')

    @deprecated(
        reason="Please replace it with Get List of Teams .https://developer.nulab.com/docs/backlog/api/2/get-list-of-teams/")
    def get_list_of_groups_raw(self, query_parameters):
        """
        Returns list of groups. ※ Deprecated API. Please replace it with Get List of Teams .https://developer.nulab.com/docs/backlog/api/2/get-list-of-teams/

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/groups',
            method='GET',
            query_parameters=query_parameters)

    @deprecated(
        reason="Please replace it with Get List of Teams .https://developer.nulab.com/docs/backlog/api/2/get-list-of-teams/")
    def get_list_of_groups(self, order=None, offset=None, count=None):
        """
        Returns list of groups. ※ Deprecated API. Please replace it with Get List of Teams .https://developer.nulab.com/docs/backlog/api/2/get-list-of-teams/

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

    @deprecated(
        reason="Please replace it with Update Team .https://developer.nulab.com/docs/backlog/api/2/update-team/")
    def update_group_raw(self, group_id, form_parameters):
        """
        Updates information about group. You can’t use this API at backlog.com space. ※ Deprecated API. Please replace it with Update Team .https://developer.nulab.com/docs/backlog/api/2/update-team/

        :param int group_id: Group ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/groups/{}'.format(group_id),
            method='PATCH',
            form_parameters=form_parameters)

    @deprecated(
        reason="Please replace it with Update Team .https://developer.nulab.com/docs/backlog/api/2/update-team/")
    def update_group(self, group_id, name=None, members=None):
        """
        Updates information about group. You can’t use this API at backlog.com space. ※ Deprecated API. Please replace it with Update Team .https://developer.nulab.com/docs/backlog/api/2/update-team/

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
