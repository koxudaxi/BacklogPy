# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Teams(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Teams, self).__init__(space_id, api_key)

    def add_group_raw(self, form_parameters):
        """
        Adds new team. You can’t use this API at backlog.com space.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/teams',
            method='POST',
            form_parameters=form_parameters)

    def add_group(self, name, members=None):
        """
        Adds new team. You can’t use this API at backlog.com space.

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
            '/teams',
            method='POST',
            form_parameters=form_parameters)

    def delete_team(self, team_id):
        """
        Deletes team. You can’t use this API at backlog.com space.

        :param int team_id: Team ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/teams/{}'.format(team_id), method='DELETE')

    def get_list_of_teams_raw(self, query_parameters):
        """
        Returns list of teams.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/teams',
            method='GET',
            query_parameters=query_parameters)

    def get_list_of_teams(self, order=None, offset=None, count=None):
        """
        Returns list of teams.

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
            '/teams',
            method='GET',
            query_parameters=query_parameters)

    def get_team(self, team_id):
        """
        Returns information about team.

        :param int team_id: Team ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/teams/{}'.format(team_id), method='GET')

    def get_team_icon(self, team_id):
        """
        Downloads team icon.

        :param int team_id: team ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/teams/{}/icon'.format(team_id), method='GET')

    def update_team_raw(self, team_id, form_parameters):
        """
        Updates information about team. You can’t use this API at backlog.com space.

        :param int team_id: Team ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/teams/{}'.format(team_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_team(self, team_id, name=None, members=None):
        """
        Updates information about team. You can’t use this API at backlog.com space.

        :param int team_id: Team ID
        :param str name: Team Name
        :param list[int] or int members: User ID added to the team

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'members[]': members
        }

        return self._request(
            '/teams/{}'.format(team_id),
            method='PATCH',
            form_parameters=form_parameters)
