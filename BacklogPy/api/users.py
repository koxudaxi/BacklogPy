# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Users(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Users, self).__init__(space_id, api_key)

    def add_user(self, form_parameters):
        """
        Adds new user to the space. “Project Administrator” cannot add “Admin” user.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users', method='POST',
                             form_parameters=form_parameters)

    def count_user_received_stars(self, query_parameters):
        """
        Returns number of stars that user received.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/:userId/stars/count',
                             method='GET', query_parameters=query_parameters)

    def count_watching(self, user_id, query_parameters):
        """
        Returns the number of your watching issues.

        :param int user_id: User ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/{}/watchings/count'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def delete_user(self, user_id):
        """
        Deletes user from the space.

        :param int user_id: user ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/{}'.format(user_id), method='DELETE')

    def get_list_of_recently_viewed_issues(self, query_parameters):
        """
        Returns list of issues which the user viewed recently.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/myself/recentlyViewedIssues',
                             method='GET', query_parameters=query_parameters)

    def get_list_of_recently_viewed_projects(self, query_parameters):
        """
        Returns list of projects which the user viewed recently.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/myself/recentlyViewedProjects',
                             method='GET', query_parameters=query_parameters)

    def get_list_of_recently_viewed_wikis(self, query_parameters):
        """
        Returns list of Wikis which the user viewed recently.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/myself/recentlyViewedWikis',
                             method='GET', query_parameters=query_parameters)

    def get_own_user(self):
        """
        Returns own information about user.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/myself', method='GET')

    def get_received_star_list(self, user_id, query_parameters):
        """
        Returns the list of stars that user received.

        :param int user_id: user ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/{}/stars'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def get_user_icon(self, user_id):
        """
        Downloads user icon.

        :param int user_id: user ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/{}/icon'.format(user_id), method='GET')

    def get_user_list(self):
        """
        Returns list of users in your space.

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users', method='GET')

    def get_user_recent_updates(self, user_id, query_parameters):
        """
        Returns user’s recent updates

        :param int user_id: user ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/{}/activities'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def get_user(self, user_id):
        """
        Returns information about user.

        :param int user_id: user ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/{}'.format(user_id), method='GET')

    def get_watching_list(self, user_id, query_parameters):
        """
        Returns list of your watching issues.

        :param int user_id: User ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/{}/watchings'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def update_user(self, user_id, form_parameters):
        """
        Updates information about user.

        :param int user_id: user ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/users/{}'.format(user_id),
                             method='PATCH', form_parameters=form_parameters)
