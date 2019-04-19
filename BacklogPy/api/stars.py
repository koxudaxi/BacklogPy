# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Stars(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Stars, self).__init__(space_id, api_key)

    def add_star_raw(self, form_parameters):
        """
        Adds star.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/stars',
            method='POST',
            form_parameters=form_parameters)

    def add_star(
            self,
            issue_id=None,
            comment_id=None,
            wiki_id=None,
            pull_request_id=None,
            pull_request_comment_id=None):
        """
        Adds star.

        :param int issue_id: Issue ID
        :param int comment_id: Comment ID
        :param int wiki_id: Wiki Page ID
        :param int pull_request_id: Pull request ID
        :param int pull_request_comment_id: Pull request comment ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'issueId': issue_id,
            'commentId': comment_id,
            'wikiId': wiki_id,
            'pullRequestId': pull_request_id,
            'pullRequestCommentId': pull_request_comment_id
        }

        return self._request(
            '/stars',
            method='POST',
            form_parameters=form_parameters)
