# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Issues(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Issues, self).__init__(space_id, api_key)

    def add_comment_raw(self, issue_id_or_key, form_parameters):
        """
        Adds a comment to the issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues/{}/comments'.format(issue_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_comment(self, issue_id_or_key, content,
                    attachment_id=None, notified_user_id=None):
        """
        Adds a comment to the issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param list[int] or int attachment_id: Attachment file ID(Post Attachment File returns)
        :param str content: Content
        :param list[int] or int notified_user_id: Notified User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'attachmentId[]': attachment_id,
            'content': content,
            'notifiedUserId[]': notified_user_id
        }

        return self._request('/issues/{}/comments'.format(issue_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_comment_notification_raw(
            self, comment_id, issue_id_or_key, form_parameters):
        """
        Adds notifications to the comment. Only the user who added the comment can add notifications.

        :param int comment_id: Comment ID
        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues/{}/comments/{}/notifications'.format(
            comment_id, issue_id_or_key), method='POST', form_parameters=form_parameters)

    def add_comment_notification(
            self, comment_id, issue_id_or_key, notified_user_id=None):
        """
        Adds notifications to the comment. Only the user who added the comment can add notifications.

        :param int comment_id: Comment ID
        :param str issue_id_or_key: Issue ID or Issue Key
        :param list[int] or int notified_user_id: UserID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'notifiedUserId[]': notified_user_id
        }

        return self._request('/issues/{}/comments/{}/notifications'.format(
            comment_id, issue_id_or_key), method='POST', form_parameters=form_parameters)

    def add_issue_raw(self, form_parameters):
        """
        Adds new issue.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues', method='POST',
                             form_parameters=form_parameters)

    def add_issue(self, issue_type_id, priority_id, project_id, summary, actual_hours=None, assignee_id=None, attachment_id=None, category_id=None,
                  description=None, due_date=None, estimated_hours=None, milestone_id=None, notified_user_id=None, parent_issue_id=None, start_date=None, version_id=None):
        """
        Adds new issue.

        :param int actual_hours: Actual Hours
        :param int assignee_id: Assignee ID
        :param list[int] or int attachment_id: Attachment file ID(Post Attachment File returns)
        :param list[int] or int category_id: Category ID
        :param str description: Description
        :param str due_date: Due Date
        :param int estimated_hours: Estimated Hours
        :param int issue_type_id: Issue Type ID
        :param list[int] or int milestone_id: Milestone ID
        :param list[int] or int notified_user_id: Notified User ID
        :param int parent_issue_id: Parent Issue ID
        :param int priority_id: Priority ID
        :param int project_id: Project ID
        :param str start_date: Start Date
        :param str summary: Summary
        :param list[int] or int version_id: Version ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'actualHours': actual_hours,
            'assigneeId': assignee_id,
            'attachmentId[]': attachment_id,
            'categoryId[]': category_id,
            'description': description,
            'dueDate': due_date,
            'estimatedHours': estimated_hours,
            'issueTypeId': issue_type_id,
            'milestoneId[]': milestone_id,
            'notifiedUserId[]': notified_user_id,
            'parentIssueId': parent_issue_id,
            'priorityId': priority_id,
            'projectId': project_id,
            'startDate': start_date,
            'summary': summary,
            'versionId[]': version_id
        }

        return self._request('/issues', method='POST',
                             form_parameters=form_parameters)

    def count_comment(self, issue_id_or_key):
        """
        Returns number of comments in issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments/count'.format(issue_id_or_key), method='GET')

    def count_issue_raw(self, query_parameters):
        """
        Returns number of issues.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues/count', method='GET',
                             query_parameters=query_parameters)

    def count_issue(self, assignee_id=None, attachment=None, category_id=None, count=None, created_since=None, created_until=None, created_user_id=None, due_date_since=None, due_date_until=None, id=None, issue_type_id=None, keyword=None, milestone_id=None, offset=None,
                    order=None, parent_child=None, parent_issue_id=None, priority_id=None, project_id=None, resolution_id=None, shared_file=None, sort=None, start_date_since=None, start_date_until=None, status_id=None, updated_since=None, updated_until=None, version_id=None):
        """
        Returns number of issues.

        :param list[int] or int assignee_id: Assignee ID
        :param bool attachment: True to make include Issue with Attachment
        :param list[int] or int category_id: Category ID
        :param int count: number of records to retrieve(1-100) default=20
        :param str created_since: Created since
        :param str created_until: Created until
        :param list[int] or int created_user_id: Created User ID
        :param str due_date_since: Due Date since
        :param str due_date_until: Due Date until
        :param list[int] or int id: Issue ID
        :param list[int] or int issue_type_id: Issue Type ID
        :param str keyword: Keyword
        :param list[int] or int milestone_id: Milestone ID
        :param int offset: offset
        :param str order: Order of the sort “asc” or “desc” default=“desc”
        :param int parent_child: Subtasking
        :param list[int] or int parent_issue_id: Parent Issue ID
        :param list[int] or int priority_id: Priority ID
        :param list[int] or int project_id: Project ID
        :param list[int] or int resolution_id: Resolution ID
        :param bool shared_file: True to make include Issue with File
        :param str sort: What to sort results by
        :param str start_date_since: Start Date since
        :param str start_date_until: Start Date until
        :param list[int] or int status_id: Status ID
        :param str updated_since: Updated since
        :param str updated_until: Updated until
        :param list[int] or int version_id: Version ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'assigneeId[]': assignee_id,
            'attachment': self._bool_to_str(attachment),
            'categoryId[]': category_id,
            'count': count,
            'createdSince': created_since,
            'createdUntil': created_until,
            'createdUserId[]': created_user_id,
            'dueDateSince': due_date_since,
            'dueDateUntil': due_date_until,
            'id[]': id,
            'issueTypeId[]': issue_type_id,
            'keyword': keyword,
            'milestoneId[]': milestone_id,
            'offset': offset,
            'order': order,
            'parentChild': parent_child,
            'parentIssueId[]': parent_issue_id,
            'priorityId[]': priority_id,
            'projectId[]': project_id,
            'resolutionId[]': resolution_id,
            'sharedFile': self._bool_to_str(shared_file),
            'sort': sort,
            'startDateSince': start_date_since,
            'startDateUntil': start_date_until,
            'statusId[]': status_id,
            'updatedSince': updated_since,
            'updatedUntil': updated_until,
            'versionId[]': version_id
        }

        return self._request('/issues/count', method='GET',
                             query_parameters=query_parameters)

    def delete_issue(self, issue_id_or_key):
        """
        Deletes issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}'.format(issue_id_or_key), method='DELETE')

    def delete_issue_attachment(self, attachment_id, issue_id_or_key):
        """
        Deletes an attachment of issue.

        :param int attachment_id: Attachment file ID
        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/attachments/{}'.format(attachment_id, issue_id_or_key), method='DELETE')

    def get_comment(self, comment_id, issue_id_or_key):
        """
        Returns information about comment.

        :param int comment_id: Comment ID
        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments/{}'.format(comment_id, issue_id_or_key), method='GET')

    def get_comment_list_raw(self, issue_id_or_key, query_parameters):
        """
        Returns list of comments in issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues/{}/comments'.format(issue_id_or_key),
                             method='GET', query_parameters=query_parameters)

    def get_comment_list(self, issue_id_or_key, count=None,
                         max_id=None, min_id=None, order=None):
        """
        Returns list of comments in issue.

        :param str issue_id_or_key: Issue ID or Issue Key
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

        return self._request('/issues/{}/comments'.format(issue_id_or_key),
                             method='GET', query_parameters=query_parameters)

    def get_issue(self, issue_id_or_key):
        """
        Returns information about issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}'.format(issue_id_or_key), method='GET')

    def get_issue_attachment(self, attachment_id, issue_id_or_key):
        """
        Downloads issue’s attachment file.

        :param int attachment_id: Attachment file ID
        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/attachments/{}'.format(attachment_id, issue_id_or_key), method='GET')

    def get_issue_list_raw(self, query_parameters):
        """
        Returns list of issues.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues', method='GET',
                             query_parameters=query_parameters)

    def get_issue_list(self, assignee_id=None, attachment=None, category_id=None, count=None, created_since=None, created_until=None, created_user_id=None, due_date_since=None, due_date_until=None, id=None, issue_type_id=None, keyword=None, milestone_id=None, offset=None,
                       order=None, parent_child=None, parent_issue_id=None, priority_id=None, project_id=None, resolution_id=None, shared_file=None, sort=None, start_date_since=None, start_date_until=None, status_id=None, updated_since=None, updated_until=None, version_id=None):
        """
        Returns list of issues.

        :param list[int] or int assignee_id: Assignee ID
        :param bool attachment: True to make include Issue with Attachment
        :param list[int] or int category_id: Category ID
        :param int count: number of records to retrieve(1-100) default=20
        :param str created_since: Created since
        :param str created_until: Created until
        :param list[int] or int created_user_id: Created User ID
        :param str due_date_since: Due Date since
        :param str due_date_until: Due Date until
        :param list[int] or int id: Issue ID
        :param list[int] or int issue_type_id: Issue Type ID
        :param str keyword: Keyword
        :param list[int] or int milestone_id: Milestone ID
        :param int offset: offset
        :param str order: Order of the sort “asc” or “desc” default=“desc”
        :param int parent_child: Subtasking
        :param list[int] or int parent_issue_id: Parent Issue ID
        :param list[int] or int priority_id: Priority ID
        :param list[int] or int project_id: Project ID
        :param list[int] or int resolution_id: Resolution ID
        :param bool shared_file: True to make include Issue with File
        :param str sort: What to sort results by
        :param str start_date_since: Start Date since
        :param str start_date_until: Start Date until
        :param list[int] or int status_id: Status ID
        :param str updated_since: Updated since
        :param str updated_until: Updated until
        :param list[int] or int version_id: Version ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'assigneeId[]': assignee_id,
            'attachment': self._bool_to_str(attachment),
            'categoryId[]': category_id,
            'count': count,
            'createdSince': created_since,
            'createdUntil': created_until,
            'createdUserId[]': created_user_id,
            'dueDateSince': due_date_since,
            'dueDateUntil': due_date_until,
            'id[]': id,
            'issueTypeId[]': issue_type_id,
            'keyword': keyword,
            'milestoneId[]': milestone_id,
            'offset': offset,
            'order': order,
            'parentChild': parent_child,
            'parentIssueId[]': parent_issue_id,
            'priorityId[]': priority_id,
            'projectId[]': project_id,
            'resolutionId[]': resolution_id,
            'sharedFile': self._bool_to_str(shared_file),
            'sort': sort,
            'startDateSince': start_date_since,
            'startDateUntil': start_date_until,
            'statusId[]': status_id,
            'updatedSince': updated_since,
            'updatedUntil': updated_until,
            'versionId[]': version_id
        }

        return self._request('/issues', method='GET',
                             query_parameters=query_parameters)

    def get_list_of_comment_notifications(self, comment_id, issue_id_or_key):
        """
        Returns the list of comment notifications.

        :param int comment_id: Comment ID
        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments/{}/notifications'.format(comment_id, issue_id_or_key), method='GET')

    def get_list_of_issue_attachments(self, issue_id_or_key):
        """
        Returns the list of issue attachments.

        :param str issue_id_or_key: Issue ID or Issue key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/attachments'.format(issue_id_or_key), method='GET')

    def get_list_of_linked_shared_files(self, issue_id_or_key):
        """
        Returns the list of linked Shared Files to issues.

        :param str issue_id_or_key: Issue ID or Issue key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/sharedFiles'.format(issue_id_or_key), method='GET')

    def link_shared_files_to_issue_raw(self, issue_id_or_key, form_parameters):
        """
        Links shared files to issue.

        :param str issue_id_or_key: Issue ID or Issue key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues/{}/sharedFiles'.format(issue_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def link_shared_files_to_issue(self, issue_id_or_key, file_id):
        """
        Links shared files to issue.

        :param str issue_id_or_key: Issue ID or Issue key
        :param list[int] or int file_id: Shared File ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'fileId[]': file_id
        }

        return self._request('/issues/{}/sharedFiles'.format(issue_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def remove_link_to_shared_file_from_issue(self, _id, issue_id_or_key):
        """
        Removes link to shared file from issue.

        :param int _id: Shared File ID
        :param str issue_id_or_key: Issue ID or Issue key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/sharedFiles/{}'.format(_id, issue_id_or_key), method='DELETE')

    def update_comment_raw(self, comment_id, issue_id_or_key, form_parameters):
        """
        Updates content of comment.

        :param int comment_id: Comment ID
        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues/{}/comments/{}'.format(comment_id,
                                                             issue_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_comment(self, comment_id, issue_id_or_key, content=None):
        """
        Updates content of comment.

        :param int comment_id: Comment ID
        :param str issue_id_or_key: Issue ID or Issue Key
        :param str content: content

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'content': content
        }

        return self._request('/issues/{}/comments/{}'.format(comment_id,
                                                             issue_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_issue_raw(self, issue_id_or_key, form_parameters):
        """
        Updates information about issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues/{}'.format(issue_id_or_key),
                             method='PATCH', form_parameters=form_parameters)

    def update_issue(self, issue_id_or_key, issue_type_id, priority_id, actual_hours=None, assignee_id=None, attachment_id=None, category_id=None, comment=None, description=None, due_date=None,
                     estimated_hours=None, milestone_id=None, notified_user_id=None, parent_issue_id=None, resolution_id=None, start_date=None, status_id=None, summary=None, version_id=None):
        """
        Updates information about issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int actual_hours: Actual Hours
        :param int assignee_id: Assignee ID
        :param list[int] or int attachment_id: Attachment file ID(Post Attachment File returns)
        :param list[int] or int category_id: Category ID
        :param str comment: Comment
        :param str description: Description
        :param str due_date: Due Date
        :param int estimated_hours: Estimated Hours
        :param int issue_type_id: Issue Type ID
        :param list[int] or int milestone_id: Milestone ID
        :param list[int] or int notified_user_id: Notified User ID
        :param int parent_issue_id: Parent Issue ID
        :param int priority_id: Priority ID
        :param int resolution_id: Resolution ID
        :param str start_date: Start Date
        :param int status_id: Status ID
        :param str summary: Summary
        :param list[int] or int version_id: Version ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'actualHours': actual_hours,
            'assigneeId': assignee_id,
            'attachmentId[]': attachment_id,
            'categoryId[]': category_id,
            'comment': comment,
            'description': description,
            'dueDate': due_date,
            'estimatedHours': estimated_hours,
            'issueTypeId': issue_type_id,
            'milestoneId[]': milestone_id,
            'notifiedUserId[]': notified_user_id,
            'parentIssueId': parent_issue_id,
            'priorityId': priority_id,
            'resolutionId': resolution_id,
            'startDate': start_date,
            'statusId': status_id,
            'summary': summary,
            'versionId[]': version_id
        }

        return self._request('/issues/{}'.format(issue_id_or_key),
                             method='PATCH', form_parameters=form_parameters)
