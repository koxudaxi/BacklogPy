# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Issues(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Issues, self).__init__(space_id, api_key)

    def add_comment_notification(self, issue_id_or_key, comment_id):
        """
        Adds notifications to the comment. Only the user who added the comment can add notifications.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/comments/{}/notifications'.format(issue_id_or_key, comment_id), method='POST')

    def add_comment(self, issue_id_or_key, form_parameters):
        """
        Adds a comment to the issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/issues/{}/comments'.format(issue_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_issue(self, form_parameters):
        """
        Adds new issue.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/issues', method='POST',
                             form_parameters=form_parameters)

    def count_comment(self, issue_id_or_key):
        """
        Returns number of comments in issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/comments/count'.format(issue_id_or_key), method='GET')

    def count_issue(self, query_parameters):
        """
        Returns number of issues.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/issues/count', method='GET',
                             query_parameters=query_parameters)

    def delete_issue_attachment(self, issue_id_or_key, attachment_id):
        """
        Deletes an attachment of issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int attachment_id: Attachment file ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/attachments/{}'.format(issue_id_or_key, attachment_id), method='DELETE')

    def delete_issue(self, issue_id_or_key):
        """
        Deletes issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}'.format(issue_id_or_key), method='DELETE')

    def get_comment_list(self, issue_id_or_key, query_parameters):
        """
        Returns list of comments in issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/issues/{}/comments'.format(issue_id_or_key),
                             method='GET', query_parameters=query_parameters)

    def get_comment(self, issue_id_or_key, comment_id):
        """
        Returns information about comment.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/comments/{}'.format(issue_id_or_key, comment_id), method='GET')

    def get_issue_attachment(self, issue_id_or_key, attachment_id):
        """
        Downloads issue’s attachment file.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int attachment_id: Attachment file ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/attachments/{}'.format(issue_id_or_key, attachment_id), method='GET')

    def get_issue_list(self, query_parameters):
        """
        Returns list of issues.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/issues', method='GET',
                             query_parameters=query_parameters)

    def get_issue(self, issue_id_or_key):
        """
        Returns information about issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}'.format(issue_id_or_key), method='GET')

    def get_list_of_comment_notifications(self, issue_id_or_key, comment_id):
        """
        Returns the list of comment notifications.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/comments/{}/notifications'.format(issue_id_or_key, comment_id), method='GET')

    def get_list_of_issue_attachments(self, issue_id_or_key):
        """
        Returns the list of issue attachments.

        :param str issue_id_or_key: Issue ID or Issue key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/attachments'.format(issue_id_or_key), method='GET')

    def get_list_of_linked_shared_files(self, issue_id_or_key):
        """
        Returns the list of linked Shared Files to issues.

        :param str issue_id_or_key: Issue ID or Issue key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/sharedFiles'.format(issue_id_or_key), method='GET')

    def link_shared_files_to_issue(self, issue_id_or_key, form_parameters):
        """
        Links shared files to issue.

        :param str issue_id_or_key: Issue ID or Issue key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/issues/{}/sharedFiles'.format(issue_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def remove_link_to_shared_file_from_issue(self, issue_id_or_key, _id):
        """
        Removes link to shared file from issue.

        :param str issue_id_or_key: Issue ID or Issue key
        :param int _id: Shared File ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/sharedFiles/{}'.format(issue_id_or_key, _id), method='DELETE')

    def update_comment(self, issue_id_or_key, comment_id):
        """
        Updates content of comment.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/issues/{}/comments/{}'.format(issue_id_or_key, comment_id), method='PATCH')

    def update_issue(self, issue_id_or_key, form_parameters):
        """
        Updates information about issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/issues/{}'.format(issue_id_or_key),
                             method='PATCH', form_parameters=form_parameters)
