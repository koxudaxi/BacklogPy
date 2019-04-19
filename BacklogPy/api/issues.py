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

        return self._request(
            '/issues/{}/comments'.format(issue_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_comment(
            self,
            issue_id_or_key,
            content,
            notified_user_id=None,
            attachment_id=None):
        """
        Adds a comment to the issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param str content: Content
        :param list[int] or int notified_user_id: Notified User ID
        :param list[int] or int attachment_id: Attachment file ID(Post Attachment File returns)

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'content': content,
            'notifiedUserId[]': notified_user_id,
            'attachmentId[]': attachment_id
        }

        return self._request(
            '/issues/{}/comments'.format(issue_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_comment_notification_raw(
            self,
            issue_id_or_key,
            comment_id,
            form_parameters):
        """
        Adds notifications to the comment. Only the user who added the comment can add notifications.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments/{}/notifications'.format(
                issue_id_or_key,
                comment_id),
            method='POST',
            form_parameters=form_parameters)

    def add_comment_notification(
            self,
            issue_id_or_key,
            comment_id,
            notified_user_id=None):
        """
        Adds notifications to the comment. Only the user who added the comment can add notifications.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID
        :param list[int] or int notified_user_id: UserID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'notifiedUserId[]': notified_user_id
        }

        return self._request(
            '/issues/{}/comments/{}/notifications'.format(
                issue_id_or_key,
                comment_id),
            method='POST',
            form_parameters=form_parameters)

    def add_issue_raw(self, form_parameters):
        """
        Adds new issue.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues',
            method='POST',
            form_parameters=form_parameters)

    def add_issue(
            self,
            project_id,
            summary,
            issue_type_id,
            priority_id,
            parent_issue_id=None,
            description=None,
            start_date=None,
            due_date=None,
            estimated_hours=None,
            actual_hours=None,
            category_id=None,
            version_id=None,
            milestone_id=None,
            assignee_id=None,
            notified_user_id=None,
            attachment_id=None):
        """
        Adds new issue.

        :param int project_id: Project ID
        :param str summary: Summary
        :param int parent_issue_id: Parent Issue ID
        :param str description: Description
        :param str start_date: Start Date (yyyy-MM-dd)
        :param str due_date: Due Date (yyyy-MM-dd)
        :param int estimated_hours: Estimated Hours
        :param int actual_hours: Actual Hours
        :param int issue_type_id: Issue Type ID
        :param list[int] or int category_id: Category ID
        :param list[int] or int version_id: Version ID
        :param list[int] or int milestone_id: Milestone ID
        :param int priority_id: Priority ID
        :param int assignee_id: Assignee ID
        :param list[int] or int notified_user_id: Notified User ID
        :param list[int] or int attachment_id: Attachment file ID(Post Attachment File returns)

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'projectId': project_id,
            'summary': summary,
            'parentIssueId': parent_issue_id,
            'description': description,
            'startDate': start_date,
            'dueDate': due_date,
            'estimatedHours': estimated_hours,
            'actualHours': actual_hours,
            'issueTypeId': issue_type_id,
            'categoryId[]': category_id,
            'versionId[]': version_id,
            'milestoneId[]': milestone_id,
            'priorityId': priority_id,
            'assigneeId': assignee_id,
            'notifiedUserId[]': notified_user_id,
            'attachmentId[]': attachment_id
        }

        return self._request(
            '/issues',
            method='POST',
            form_parameters=form_parameters)

    def count_comment(self, issue_id_or_key):
        """
        Returns number of comments in issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments/count'.format(issue_id_or_key),
            method='GET')

    def count_issue_raw(self, query_parameters):
        """
        Returns number of issues.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/count',
            method='GET',
            query_parameters=query_parameters)

    def count_issue(
            self,
            project_id=None,
            issue_type_id=None,
            category_id=None,
            version_id=None,
            milestone_id=None,
            status_id=None,
            priority_id=None,
            assignee_id=None,
            created_user_id=None,
            resolution_id=None,
            parent_child=None,
            attachment=None,
            shared_file=None,
            sort=None,
            order=None,
            offset=None,
            count=None,
            created_since=None,
            created_until=None,
            updated_since=None,
            updated_until=None,
            start_date_since=None,
            start_date_until=None,
            due_date_since=None,
            due_date_until=None,
            id=None,
            parent_issue_id=None,
            keyword=None):
        """
        Returns number of issues.

        :param list[int] or int project_id: Project ID
        :param list[int] or int issue_type_id: Issue Type ID
        :param list[int] or int category_id: Category ID
        :param list[int] or int version_id: Version ID
        :param list[int] or int milestone_id: Milestone ID
        :param list[int] or int status_id: Status ID
        :param list[int] or int priority_id: Priority ID
        :param list[int] or int assignee_id: Assignee ID
        :param list[int] or int created_user_id: Created User ID
        :param list[int] or int resolution_id: Resolution ID
        :param int parent_child: Subtasking
        :param bool attachment: True to make include Issue with Attachment
        :param bool shared_file: True to make include Issue with File
        :param str sort: What to sort results by
        :param str order: Order of the sort “asc” or “desc” default=“desc”
        :param int offset: offset
        :param int count: number of records to retrieve(1-100) default=20
        :param str created_since: Created since (yyyy-MM-dd)
        :param str created_until: Created until (yyyy-MM-dd)
        :param str updated_since: Updated since (yyyy-MM-dd)
        :param str updated_until: Updated until (yyyy-MM-dd)
        :param str start_date_since: Start Date since (yyyy-MM-dd)
        :param str start_date_until: Start Date until (yyyy-MM-dd)
        :param str due_date_since: Due Date since (yyyy-MM-dd)
        :param str due_date_until: Due Date until (yyyy-MM-dd)
        :param list[int] or int id: Issue ID
        :param list[int] or int parent_issue_id: Parent Issue ID
        :param str keyword: Keyword

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'projectId[]': project_id,
            'issueTypeId[]': issue_type_id,
            'categoryId[]': category_id,
            'versionId[]': version_id,
            'milestoneId[]': milestone_id,
            'statusId[]': status_id,
            'priorityId[]': priority_id,
            'assigneeId[]': assignee_id,
            'createdUserId[]': created_user_id,
            'resolutionId[]': resolution_id,
            'parentChild': parent_child,
            'attachment': self._bool_to_str(attachment),
            'sharedFile': self._bool_to_str(shared_file),
            'sort': sort,
            'order': order,
            'offset': offset,
            'count': count,
            'createdSince': created_since,
            'createdUntil': created_until,
            'updatedSince': updated_since,
            'updatedUntil': updated_until,
            'startDateSince': start_date_since,
            'startDateUntil': start_date_until,
            'dueDateSince': due_date_since,
            'dueDateUntil': due_date_until,
            'id[]': id,
            'parentIssueId[]': parent_issue_id,
            'keyword': keyword
        }

        return self._request(
            '/issues/count',
            method='GET',
            query_parameters=query_parameters)

    def delete_comment(self, issue_id_or_key, comment_id):
        """
        Delete comment.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/issues/{}/comments/{}'.format(issue_id_or_key,
                                                             comment_id), method='DELETE                              ')

    def delete_issue(self, issue_id_or_key):
        """
        Deletes issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}'.format(issue_id_or_key),
            method='DELETE')

    def delete_issue_attachment(self, issue_id_or_key, attachment_id):
        """
        Deletes an attachment of issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int attachment_id: Attachment file ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/attachments/{}'.format(issue_id_or_key, attachment_id), method='DELETE')

    def get_comment(self, issue_id_or_key, comment_id):
        """
        Returns information about comment.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments/{}'.format(issue_id_or_key, comment_id), method='GET')

    def get_comment_list_raw(self, issue_id_or_key, query_parameters):
        """
        Returns list of comments in issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments'.format(issue_id_or_key),
            method='GET',
            query_parameters=query_parameters)

    def get_comment_list(
            self,
            issue_id_or_key,
            min_id=None,
            max_id=None,
            count=None,
            order=None):
        """
        Returns list of comments in issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int min_id: minimum ID
        :param int max_id: maximum ID
        :param int count: number of records to retrieve(1-100) default=20
        :param str order: “asc” or “desc” default=“desc”

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'minId': min_id,
            'maxId': max_id,
            'count': count,
            'order': order
        }

        return self._request(
            '/issues/{}/comments'.format(issue_id_or_key),
            method='GET',
            query_parameters=query_parameters)

    def get_issue(self, issue_id_or_key):
        """
        Returns information about issue.

        :param str issue_id_or_key: Issue ID or Issue Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}'.format(issue_id_or_key),
            method='GET')

    def get_issue_attachment(self, issue_id_or_key, attachment_id):
        """
        Downloads issue’s attachment file.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int attachment_id: Attachment file ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/attachments/{}'.format(issue_id_or_key, attachment_id), method='GET')

    def get_issue_list_raw(self, query_parameters):
        """
        Returns list of issues.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues',
            method='GET',
            query_parameters=query_parameters)

    def get_issue_list(
            self,
            project_id=None,
            issue_type_id=None,
            category_id=None,
            version_id=None,
            milestone_id=None,
            status_id=None,
            priority_id=None,
            assignee_id=None,
            created_user_id=None,
            resolution_id=None,
            parent_child=None,
            attachment=None,
            shared_file=None,
            sort=None,
            order=None,
            offset=None,
            count=None,
            created_since=None,
            created_until=None,
            updated_since=None,
            updated_until=None,
            start_date_since=None,
            start_date_until=None,
            due_date_since=None,
            due_date_until=None,
            id=None,
            parent_issue_id=None,
            keyword=None):
        """
        Returns list of issues.

        :param list[int] or int project_id: Project ID
        :param list[int] or int issue_type_id: Issue Type ID
        :param list[int] or int category_id: Category ID
        :param list[int] or int version_id: Version ID
        :param list[int] or int milestone_id: Milestone ID
        :param list[int] or int status_id: Status ID
        :param list[int] or int priority_id: Priority ID
        :param list[int] or int assignee_id: Assignee ID
        :param list[int] or int created_user_id: Created User ID
        :param list[int] or int resolution_id: Resolution ID
        :param int parent_child: Subtasking
        :param bool attachment: True to make include Issue with Attachment
        :param bool shared_file: True to make include Issue with File
        :param str sort: What to sort results by
        :param str order: Order of the sort “asc” or “desc” default=“desc”
        :param int offset: offset
        :param int count: number of records to retrieve(1-100) default=20
        :param str created_since: Created since (yyyy-MM-dd)
        :param str created_until: Created until (yyyy-MM-dd)
        :param str updated_since: Updated since (yyyy-MM-dd)
        :param str updated_until: Updated until (yyyy-MM-dd)
        :param str start_date_since: Start Date since (yyyy-MM-dd)
        :param str start_date_until: Start Date until (yyyy-MM-dd)
        :param str due_date_since: Due Date since (yyyy-MM-dd)
        :param str due_date_until: Due Date until (yyyy-MM-dd)
        :param list[int] or int id: Issue ID
        :param list[int] or int parent_issue_id: Parent Issue ID
        :param str keyword: Keyword

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'projectId[]': project_id,
            'issueTypeId[]': issue_type_id,
            'categoryId[]': category_id,
            'versionId[]': version_id,
            'milestoneId[]': milestone_id,
            'statusId[]': status_id,
            'priorityId[]': priority_id,
            'assigneeId[]': assignee_id,
            'createdUserId[]': created_user_id,
            'resolutionId[]': resolution_id,
            'parentChild': parent_child,
            'attachment': self._bool_to_str(attachment),
            'sharedFile': self._bool_to_str(shared_file),
            'sort': sort,
            'order': order,
            'offset': offset,
            'count': count,
            'createdSince': created_since,
            'createdUntil': created_until,
            'updatedSince': updated_since,
            'updatedUntil': updated_until,
            'startDateSince': start_date_since,
            'startDateUntil': start_date_until,
            'dueDateSince': due_date_since,
            'dueDateUntil': due_date_until,
            'id[]': id,
            'parentIssueId[]': parent_issue_id,
            'keyword': keyword
        }

        return self._request(
            '/issues',
            method='GET',
            query_parameters=query_parameters)

    def get_list_of_comment_notifications(self, issue_id_or_key, comment_id):
        """
        Returns the list of comment notifications.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments/{}/notifications'.format(issue_id_or_key, comment_id), method='GET')

    def get_list_of_issue_attachments(self, issue_id_or_key):
        """
        Returns the list of issue attachments.

        :param str issue_id_or_key: Issue ID or Issue key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/attachments'.format(issue_id_or_key),
            method='GET')

    def get_list_of_linked_shared_files(self, issue_id_or_key):
        """
        Returns the list of linked Shared Files to issues.

        :param str issue_id_or_key: Issue ID or Issue key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/sharedFiles'.format(issue_id_or_key),
            method='GET')

    def link_shared_files_to_issue_raw(self, issue_id_or_key, form_parameters):
        """
        Links shared files to issue.

        :param str issue_id_or_key: Issue ID or Issue key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/sharedFiles'.format(issue_id_or_key),
            method='POST',
            form_parameters=form_parameters)

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

        return self._request(
            '/issues/{}/sharedFiles'.format(issue_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def remove_link_to_shared_file_from_issue(self, issue_id_or_key, _id):
        """
        Removes link to shared file from issue.

        :param str issue_id_or_key: Issue ID or Issue key
        :param int _id: Shared File ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/sharedFiles/{}'.format(issue_id_or_key, _id), method='DELETE')

    def update_comment_raw(self, issue_id_or_key, comment_id, form_parameters):
        """
        Updates content of comment.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}/comments/{}'.format(
                issue_id_or_key,
                comment_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_comment(self, issue_id_or_key, comment_id, content=None):
        """
        Updates content of comment.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param int comment_id: Comment ID
        :param str content: content

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'content': content
        }

        return self._request(
            '/issues/{}/comments/{}'.format(
                issue_id_or_key,
                comment_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_issue_raw(self, issue_id_or_key, form_parameters):
        """
        Updates information about issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/issues/{}'.format(issue_id_or_key),
            method='PATCH',
            form_parameters=form_parameters)

    def update_issue(
            self,
            issue_id_or_key,
            issue_type_id,
            priority_id,
            summary=None,
            parent_issue_id=None,
            description=None,
            status_id=None,
            resolution_id=None,
            start_date=None,
            due_date=None,
            estimated_hours=None,
            actual_hours=None,
            category_id=None,
            version_id=None,
            milestone_id=None,
            assignee_id=None,
            notified_user_id=None,
            attachment_id=None,
            comment=None):
        """
        Updates information about issue.

        :param str issue_id_or_key: Issue ID or Issue Key
        :param str summary: Summary
        :param int parent_issue_id: Parent Issue ID
        :param str description: Description
        :param int status_id: Status ID
        :param int resolution_id: Resolution ID
        :param str start_date: Start Date (yyyy-MM-dd)
        :param str due_date: Due Date (yyyy-MM-dd)
        :param int estimated_hours: Estimated Hours
        :param int actual_hours: Actual Hours
        :param int issue_type_id: Issue Type ID
        :param list[int] or int category_id: Category ID
        :param list[int] or int version_id: Version ID
        :param list[int] or int milestone_id: Milestone ID
        :param int priority_id: Priority ID
        :param int assignee_id: Assignee ID
        :param list[int] or int notified_user_id: Notified User ID
        :param list[int] or int attachment_id: Attachment file ID(Post Attachment File returns)
        :param str comment: Comment

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'summary': summary,
            'parentIssueId': parent_issue_id,
            'description': description,
            'statusId': status_id,
            'resolutionId': resolution_id,
            'startDate': start_date,
            'dueDate': due_date,
            'estimatedHours': estimated_hours,
            'actualHours': actual_hours,
            'issueTypeId': issue_type_id,
            'categoryId[]': category_id,
            'versionId[]': version_id,
            'milestoneId[]': milestone_id,
            'priorityId': priority_id,
            'assigneeId': assignee_id,
            'notifiedUserId[]': notified_user_id,
            'attachmentId[]': attachment_id,
            'comment': comment
        }

        return self._request(
            '/issues/{}'.format(issue_id_or_key),
            method='PATCH',
            form_parameters=form_parameters)
