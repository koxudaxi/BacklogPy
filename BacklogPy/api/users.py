# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Users(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Users, self).__init__(space_id, api_key)

    def add_user_raw(self, form_parameters):
        """
        Adds new user to the space. “Project Administrator” cannot add “Admin” user.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users', method='POST',
                             form_parameters=form_parameters)

    def add_user(self, mail_address, name, password, role_type, user_id):
        """
        Adds new user to the space. “Project Administrator” cannot add “Admin” user.

        :param str mail_address: Email address
        :param str name: nickname
        :param str password: password
        :param int role_type: Administrator(1) Normal User(2) Reporter(3) Viewer(4) Guest Reporter(5) Guest Viewer(6)
        :param str user_id: user ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'mailAddress': mail_address,
            'name': name,
            'password': password,
            'roleType': role_type,
            'userId': user_id
        }

        return self._request('/users', method='POST',
                             form_parameters=form_parameters)

    def count_user_received_stars_raw(self, query_parameters):
        """
        Returns number of stars that user received.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/:userId/stars/count',
                             method='GET', query_parameters=query_parameters)

    def count_user_received_stars(self, since=None, until=None):
        """
        Returns number of stars that user received.

        :param str since: after the given date (YYYY-MM-DD)
        :param str until: before the given date (YYYY-MM-DD)

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'since': since,
            'until': until
        }

        return self._request('/users/:userId/stars/count',
                             method='GET', query_parameters=query_parameters)

    def count_watching_raw(self, user_id, query_parameters):
        """
        Returns the number of your watching issues.

        :param int user_id: User ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/{}/watchings/count'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def count_watching(self, user_id, already_read=None,
                       resource_already_read=None):
        """
        Returns the number of your watching issues.

        :param int user_id: User ID
        :param bool already_read: This parameter is optional. Set this parameter to false to get unread watching count since the last time checked by user and true for already read watching count. When both alreadyRead and resourceAlreadyRead parameters set, resourceAlreadyRead will be ignored.
        :param bool resource_already_read: This parameter is optional. Set to false for unread watching count and true for already read watching count.

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'alreadyRead': self._bool_to_str(already_read),
            'resourceAlreadyRead': self._bool_to_str(resource_already_read)
        }

        return self._request('/users/{}/watchings/count'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def delete_user(self, user_id):
        """
        Deletes user from the space.

        :param int user_id: user ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/{}'.format(user_id), method='DELETE')

    def get_list_of_recently_viewed_issues_raw(self, query_parameters):
        """
        Returns list of issues which the user viewed recently.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/myself/recentlyViewedIssues',
                             method='GET', query_parameters=query_parameters)

    def get_list_of_recently_viewed_issues(
            self, count=None, offset=None, order=None):
        """
        Returns list of issues which the user viewed recently.

        :param int count: number of records to retrieve(1-100) default=20
        :param int offset: offset
        :param str order: “asc” or “desc” default=“desc”

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'count': count,
            'offset': offset,
            'order': order
        }

        return self._request('/users/myself/recentlyViewedIssues',
                             method='GET', query_parameters=query_parameters)

    def get_list_of_recently_viewed_projects_raw(self, query_parameters):
        """
        Returns list of projects which the user viewed recently.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/myself/recentlyViewedProjects',
                             method='GET', query_parameters=query_parameters)

    def get_list_of_recently_viewed_projects(
            self, count=None, offset=None, order=None):
        """
        Returns list of projects which the user viewed recently.

        :param int count: number of records to retrieve(1-100) default=20
        :param int offset: offset
        :param str order: “asc” or “desc” default=“desc”

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'count': count,
            'offset': offset,
            'order': order
        }

        return self._request('/users/myself/recentlyViewedProjects',
                             method='GET', query_parameters=query_parameters)

    def get_list_of_recently_viewed_wikis_raw(self, query_parameters):
        """
        Returns list of Wikis which the user viewed recently.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/myself/recentlyViewedWikis',
                             method='GET', query_parameters=query_parameters)

    def get_list_of_recently_viewed_wikis(
            self, count=None, offset=None, order=None):
        """
        Returns list of Wikis which the user viewed recently.

        :param int count: number of records to retrieve(1-100) default=20
        :param int offset: offset
        :param str order: “asc” or “desc” default=“desc”

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'count': count,
            'offset': offset,
            'order': order
        }

        return self._request('/users/myself/recentlyViewedWikis',
                             method='GET', query_parameters=query_parameters)

    def get_own_user(self):
        """
        Returns own information about user.

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/myself', method='GET')

    def get_received_star_list_raw(self, user_id, query_parameters):
        """
        Returns the list of stars that user received.

        :param int user_id: user ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/{}/stars'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def get_received_star_list(
            self, user_id, count=None, max_id=None, min_id=None, order=None):
        """
        Returns the list of stars that user received.

        :param int user_id: user ID
        :param int count: number of records to retrieve(1-100) default=20
        :param int max_id: maximum ID
        :param int min_id: minimum ID
        :param str order: “asc” or “desc” default=“desc”

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'count': count,
            'maxId': max_id,
            'minId': min_id,
            'order': order
        }

        return self._request('/users/{}/stars'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def get_user(self, user_id):
        """
        Returns information about user.

        :param int user_id: user ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/{}'.format(user_id), method='GET')

    def get_user_icon(self, user_id):
        """
        Downloads user icon.

        :param int user_id: user ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/{}/icon'.format(user_id), method='GET')

    def get_user_list(self):
        """
        Returns list of users in your space.

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users', method='GET')

    def get_user_recent_updates_raw(self, user_id, query_parameters):
        """
        Returns user’s recent updates

        :param int user_id: user ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/{}/activities'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def get_user_recent_updates(
            self, user_id, activity_type_id=None, count=None, max_id=None, min_id=None, order=None):
        """
        Returns user’s recent updates

        :param int user_id: user ID
        :param list[int] or int activity_type_id: type(1-17)
        :param int count: number of records to retrieve(1-100) default=20
        :param int max_id: maximum ID
        :param int min_id: minimum ID
        :param str order: “asc” or “desc” default=“desc”

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'activityTypeId[]': activity_type_id,
            'count': count,
            'maxId': max_id,
            'minId': min_id,
            'order': order
        }

        return self._request('/users/{}/activities'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def get_watching_list_raw(self, user_id, query_parameters):
        """
        Returns list of your watching issues.

        :param int user_id: User ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/{}/watchings'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def get_watching_list(self, user_id, count=None, issue_id=None,
                          offset=None, order=None, resource_already_read=None, sort=None):
        """
        Returns list of your watching issues.

        :param int user_id: User ID
        :param int count: Number of records to retrieve(1-100) default=20
        :param list[int] or int issue_id: Issue ID
        :param int offset: Where to start returning records from the entire results. default=0
        :param str order: Order of the sort “asc” or “desc” default=“desc”
        :param bool resource_already_read: Whether the issues already read are retrieved or not. The all watching issues are returned if this parameter is omitted. The read watching issues are returned if true. The unread watching issues are returned if false. default=null
        :param str sort: What to sort results by. The value “created”, “updated” or “issueUpdated” are allowed. default=“issueUpdated”

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'count': count,
            'issueId[]': issue_id,
            'offset': offset,
            'order': order,
            'resourceAlreadyRead': self._bool_to_str(resource_already_read),
            'sort': sort
        }

        return self._request('/users/{}/watchings'.format(user_id),
                             method='GET', query_parameters=query_parameters)

    def update_user_raw(self, user_id, form_parameters):
        """
        Updates information about user.

        :param int user_id: user ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/users/{}'.format(user_id),
                             method='PATCH', form_parameters=form_parameters)

    def update_user(self, user_id, mail_address=None,
                    name=None, password=None, role_type=None):
        """
        Updates information about user.

        :param int user_id: user ID
        :param str mail_address: Email address
        :param str name: nickname
        :param str password: password
        :param int role_type: Administrator(1) Normal User(2) Reporter(3) Viewer(4) Guest Reporter(5) Guest Viewer(6)

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'mailAddress': mail_address,
            'name': name,
            'password': password,
            'roleType': role_type
        }

        return self._request('/users/{}'.format(user_id),
                             method='PATCH', form_parameters=form_parameters)
