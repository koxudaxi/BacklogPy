# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Projects(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Projects, self).__init__(space_id, api_key)

    def add_category_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Category to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/categories'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_category(self, project_id_or_key, name):
        """
        Adds new Category to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param str name: Category name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name
        }

        return self._request('/projects/{}/categories'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_custom_field_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Custom Field to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/customFields'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_custom_field(self, project_id_or_key, name, type_id,
                         applicable_issue_types=None, description=None, required=None):
        """
        Adds new Custom Field to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param list[int] or int applicable_issue_types: Type ID to enable Custom fields
        :param str description: Description
        :param str name: Name
        :param bool required: True to make the Custom field required
        :param int type_id: Type ID of Custom field

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'applicableIssueTypes[]': applicable_issue_types,
            'description': description,
            'name': name,
            'required': self._bool_to_str(required),
            'typeId': type_id
        }

        return self._request('/projects/{}/customFields'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_issue_type_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Issue Type to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/issueTypes'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_issue_type(self, project_id_or_key, color, name):
        """
        Adds new Issue Type to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param str color: Background color
        :param str name: Issue Type name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'color': color,
            'name': name
        }

        return self._request('/projects/{}/issueTypes'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_list_item_for_list_type_custom_field_raw(
            self, _id, project_id_or_key, form_parameters):
        """
        Adds new list item for list type custom field. Only administrator can call this API if the option “Add items in adding or editing issues” is disabled in settings. Calling API fails if specified custom field’s type is not a list.

        :param int _id: Custom field ID
        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/customFields/{}/items'.format(
            _id, project_id_or_key), method='POST', form_parameters=form_parameters)

    def add_list_item_for_list_type_custom_field(
            self, _id, project_id_or_key, name=None):
        """
        Adds new list item for list type custom field. Only administrator can call this API if the option “Add items in adding or editing issues” is disabled in settings. Calling API fails if specified custom field’s type is not a list.

        :param int _id: Custom field ID
        :param str project_id_or_key: Project ID or Project Key
        :param str name: List item name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name
        }

        return self._request('/projects/{}/customFields/{}/items'.format(
            _id, project_id_or_key), method='POST', form_parameters=form_parameters)

    def add_project_raw(self, form_parameters):
        """
        Adds new project.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects', method='POST',
                             form_parameters=form_parameters)

    def add_project(self, chart_enabled, key, name, subtasking_enabled,
                    text_formatting_rule, project_leader_can_edit_project_leader=None):
        """
        Adds new project.

        :param bool chart_enabled: Enable chart
        :param str key: Project Key
        :param str name: Project Name
        :param bool project_leader_can_edit_project_leader: Allow project administrators to manage each other
        :param bool subtasking_enabled: Enable subtasking
        :param str text_formatting_rule: Formatting rules “backlog” or “markdown”

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'chartEnabled': self._bool_to_str(chart_enabled),
            'key': key,
            'name': name,
            'projectLeaderCanEditProjectLeader': self._bool_to_str(project_leader_can_edit_project_leader),
            'subtaskingEnabled': self._bool_to_str(subtasking_enabled),
            'textFormattingRule': text_formatting_rule
        }

        return self._request('/projects', method='POST',
                             form_parameters=form_parameters)

    def add_project_administrator_raw(
            self, project_id_or_key, form_parameters):
        """
        Adds “Project Administrator” role to user

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/administrators'.format(
            project_id_or_key), method='POST', form_parameters=form_parameters)

    def add_project_administrator(self, project_id_or_key, user_id=None):
        """
        Adds “Project Administrator” role to user

        :param str project_id_or_key: Project ID or Project Key
        :param int user_id: User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'userId': user_id
        }

        return self._request('/projects/{}/administrators'.format(
            project_id_or_key), method='POST', form_parameters=form_parameters)

    def add_project_user_raw(self, project_id_or_key, form_parameters):
        """
        Adds user to list of project members.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/users'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_project_user(self, project_id_or_key, user_id=None):
        """
        Adds user to list of project members.

        :param str project_id_or_key: Project ID or Project Key
        :param int user_id: User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'userId': user_id
        }

        return self._request('/projects/{}/users'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_pull_request_raw(self, project_id_or_key,
                             repo_id_or_name, form_parameters):
        """
        Adds pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests'.format(
            project_id_or_key, repo_id_or_name), method='POST', form_parameters=form_parameters)

    def add_pull_request(self, project_id_or_key, repo_id_or_name, summary, assignee_id=None,
                         attachment_id=None, base=None, branch=None, description=None, issue_id=None, notified_user_id=None):
        """
        Adds pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int assignee_id: Assignee’s ID of pull request
        :param list[int] or int attachment_id: ID returned by “Post Attachment File” API
        :param str base: Branch name of merge base
        :param str branch: Name of merging branch
        :param str description: Description of pull request
        :param int issue_id: Related issue’s ID
        :param list[int] or int notified_user_id: User ID to send notification when pull request is added
        :param str summary: Summary of pull request

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'assigneeId': assignee_id,
            'attachmentId[]': attachment_id,
            'base': base,
            'branch': branch,
            'description': description,
            'issueId': issue_id,
            'notifiedUserId[]': notified_user_id,
            'summary': summary
        }

        return self._request('/projects/{}/git/repositories/{}/pullRequests'.format(
            project_id_or_key, repo_id_or_name), method='POST', form_parameters=form_parameters)

    def add_pull_request_comment_raw(
            self, number, project_id_or_key, repo_id_or_name, form_parameters):
        """
        Adds comments on pull requests.

        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
            number, project_id_or_key, repo_id_or_name), method='POST', form_parameters=form_parameters)

    def add_pull_request_comment(
            self, number, project_id_or_key, repo_id_or_name, content, notified_user_id=None):
        """
        Adds comments on pull requests.

        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param str content: Comment
        :param list[int] or int notified_user_id: User ID to send notification when comment is added

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'content': content,
            'notifiedUserId[]': notified_user_id
        }

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
            number, project_id_or_key, repo_id_or_name), method='POST', form_parameters=form_parameters)

    def add_version_milestone_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Version/Milestone to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/versions'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_version_milestone(self, project_id_or_key, name,
                              description=None, release_due_date=None, start_date=None):
        """
        Adds new Version/Milestone to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param str description: Version description
        :param str name: Version name
        :param str release_due_date: Release Due Date
        :param str start_date: Start Date

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'description': description,
            'name': name,
            'releaseDueDate': release_due_date,
            'startDate': start_date
        }

        return self._request('/projects/{}/versions'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_webhook_raw(self, project_id_or_key, form_parameters):
        """
        Adds new webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/webhooks'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_webhook(self, project_id_or_key, activity_type_ids=None,
                    all_event=None, description=None, hook_url=None, name=None):
        """
        Adds new webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param list[int] or int activity_type_ids: Event ID to be notified
        :param bool all_event: True to make all events notified
        :param str description: Description
        :param str hook_url: hook URL
        :param str name: Name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'activityTypeIds[]': activity_type_ids,
            'allEvent': self._bool_to_str(all_event),
            'description': description,
            'hookUrl': hook_url,
            'name': name
        }

        return self._request('/projects/{}/webhooks'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def delete_category(self, _id, project_id_or_key):
        """
        Deletes Category.

        :param int _id: Category ID
        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/categories/{}'.format(_id, project_id_or_key), method='DELETE')

    def delete_custom_field(self, _id, project_id_or_key):
        """
        Deletes Custom Field.

        :param int _id: Custom field ID
        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields/{}'.format(_id, project_id_or_key), method='DELETE')

    def delete_issue_type_raw(self, _id, project_id_or_key, form_parameters):
        """
        Deletes Issue Type.

        :param int _id: Issue Type ID
        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/issueTypes/{}'.format(
            _id, project_id_or_key), method='DELETE', form_parameters=form_parameters)

    def delete_issue_type(self, _id, project_id_or_key,
                          substitute_issue_type_id):
        """
        Deletes Issue Type.

        :param int _id: Issue Type ID
        :param str project_id_or_key: Project ID or Project Key
        :param int substitute_issue_type_id: type ID to change linked issue

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'substituteIssueTypeId': substitute_issue_type_id
        }

        return self._request('/projects/{}/issueTypes/{}'.format(
            _id, project_id_or_key), method='DELETE', form_parameters=form_parameters)

    def delete_list_item_for_list_type_custom_field(
            self, _id, item_id, project_id_or_key):
        """
        Deletes list item for list type custom field. Calling API fails if specified custom field’s type is not a list.

        :param int _id: Custom field ID
        :param int item_id: List item ID
        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/customFields/{}/items/{}'.format(
            _id, item_id, project_id_or_key), method='DELETE')

    def delete_project(self, project_id_or_key):
        """
        Deletes project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}'.format(project_id_or_key), method='DELETE')

    def delete_project_administrator_raw(
            self, project_id_or_key, form_parameters):
        """
        Removes Project Administrator role from user

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/administrators'.format(
            project_id_or_key), method='DELETE', form_parameters=form_parameters)

    def delete_project_administrator(self, project_id_or_key, user_id=None):
        """
        Removes Project Administrator role from user

        :param str project_id_or_key: Project ID or Project Key
        :param int user_id: User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'userId': user_id
        }

        return self._request('/projects/{}/administrators'.format(
            project_id_or_key), method='DELETE', form_parameters=form_parameters)

    def delete_project_user_raw(self, project_id_or_key, form_parameters):
        """
        Removes user from list project members.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/users'.format(project_id_or_key),
                             method='DELETE', form_parameters=form_parameters)

    def delete_project_user(self, project_id_or_key, user_id=None):
        """
        Removes user from list project members.

        :param str project_id_or_key: Project ID or Project Key
        :param int user_id: User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'userId': user_id
        }

        return self._request('/projects/{}/users'.format(project_id_or_key),
                             method='DELETE', form_parameters=form_parameters)

    def delete_pull_request_attachments(
            self, attachment_id, number, project_id_or_key, repo_id_or_name):
        """
        Deletes attached files on pull requests.

        :param int attachment_id: Attached file’s ID
        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/attachments/{}'.format(
            attachment_id, number, project_id_or_key, repo_id_or_name), method='DELETE')

    def delete_version(self, _id, project_id_or_key):
        """
        Deletes Version.

        :param int _id: Version のID
        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/versions/{}'.format(_id, project_id_or_key), method='DELETE')

    def delete_webhook(self, project_id_or_key, webhook_id):
        """
        Deletes webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/webhooks/{}'.format(project_id_or_key, webhook_id), method='DELETE')

    def download_pull_request_attachment(
            self, attachment_id, number, project_id_or_key, repo_id_or_name):
        """
        Downloads attached files on pull requests.

        :param int attachment_id: Attached file’s ID
        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/attachments/{}'.format(
            attachment_id, number, project_id_or_key, repo_id_or_name), method='GET')

    def get_category_list(self, project_id_or_key):
        """
        Returns list of Categories in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/categories'.format(project_id_or_key), method='GET')

    def get_custom_field_list(self, project_id_or_key):
        """
        Returns list of Custom Fields in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields'.format(project_id_or_key), method='GET')

    def get_file(self, _id, project_id_or_key):
        """
        Downloads the file.

        :param int _id: File ID
        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/files/{}'.format(_id, project_id_or_key), method='GET')

    def get_git_repository(self, project_id_or_key, repo_id_or_name):
        """
        Returns Git repository.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}'.format(project_id_or_key, repo_id_or_name), method='GET')

    def get_issue_type_list(self, project_id_or_key):
        """
        Returns list of Issue Types in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/issueTypes'.format(project_id_or_key), method='GET')

    def get_list_of_git_repositories(self, project_id_or_key):
        """
        Returns list of Git repositories.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories'.format(project_id_or_key), method='GET')

    def get_list_of_project_administrators(self, project_id_or_key):
        """
        Returns list of users who has Project Administrator role

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/administrators'.format(project_id_or_key), method='GET')

    def get_list_of_pull_request_attachment(
            self, number, project_id_or_key, repo_id_or_name):
        """
        Returns list of attached files on pull requests.

        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/attachments'.format(
            number, project_id_or_key, repo_id_or_name), method='GET')

    def get_list_of_shared_files_raw(
            self, path, project_id_or_key, query_parameters):
        """
        Gets list of Shared Files.

        :param str path: Directory path
        :param str project_id_or_key: Project ID or Project key
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/files/metadata/{}'.format(path,
                                                                     project_id_or_key), method='GET', query_parameters=query_parameters)

    def get_list_of_shared_files(
            self, path, project_id_or_key, count=None, offset=None, order=None):
        """
        Gets list of Shared Files.

        :param str path: Directory path
        :param str project_id_or_key: Project ID or Project key
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

        return self._request('/projects/{}/files/metadata/{}'.format(path,
                                                                     project_id_or_key), method='GET', query_parameters=query_parameters)

    def get_list_of_webhooks(self, project_id_or_key):
        """
        Returns list of webhooks.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/webhooks'.format(project_id_or_key), method='GET')

    def get_number_of_pull_request_comments(
            self, number, project_id_or_key, repo_id_or_name):
        """
        Returns number of comments on pull requests.

        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments/count'.format(
            number, project_id_or_key, repo_id_or_name), method='GET')

    def get_number_of_pull_requests(self, project_id_or_key, repo_id_or_name):
        """
        Returns number of pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/count'.format(
            project_id_or_key, repo_id_or_name), method='GET')

    def get_project(self, project_id_or_key):
        """
        Returns information about project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}'.format(project_id_or_key), method='GET')

    def get_project_disk_usage(self, project_id_or_key):
        """
        Returns information about project disk usage.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/diskUsage'.format(project_id_or_key), method='GET')

    def get_project_icon(self, project_id_or_key):
        """
        Downloads project icon.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/image'.format(project_id_or_key), method='GET')

    def get_project_list_raw(self, query_parameters):
        """
        Returns list of projects.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects', method='GET',
                             query_parameters=query_parameters)

    def get_project_list(self, all=None, archived=None):
        """
        Returns list of projects.

        :param bool all: Only applies to administrators. If ‘true,’ it returns all projects. If ‘false,’ it returns only projects they have joined (set to ‘false’ by default).
        :param bool archived: For unspecified parameters, this form returns all projects. For ‘false’ parameters, it returns unarchived projects. For ‘true’ parameters, it returns archived projects.

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'all': self._bool_to_str(all),
            'archived': self._bool_to_str(archived)
        }

        return self._request('/projects', method='GET',
                             query_parameters=query_parameters)

    def get_project_recent_updates_raw(
            self, project_id_or_key, query_parameters):
        """
        Returns recent update in the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/activities'.format(project_id_or_key),
                             method='GET', query_parameters=query_parameters)

    def get_project_recent_updates(
            self, project_id_or_key, activity_type_id=None, count=None, max_id=None, min_id=None, order=None):
        """
        Returns recent update in the project.

        :param str project_id_or_key: Project ID or Project Key
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

        return self._request('/projects/{}/activities'.format(project_id_or_key),
                             method='GET', query_parameters=query_parameters)

    def get_project_user_list(self, project_id_or_key):
        """
        Returns list of project members.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/users'.format(project_id_or_key), method='GET')

    def get_pull_request(self, number, project_id_or_key, repo_id_or_name):
        """
        Returns pull reuqest.

        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}'.format(
            number, project_id_or_key, repo_id_or_name), method='GET')

    def get_pull_request_comment(
            self, number, project_id_or_key, repo_id_or_name):
        """
        Returns list of pull request comments.

        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
            number, project_id_or_key, repo_id_or_name), method='GET')

    def get_pull_request_list(self, project_id_or_key, repo_id_or_name):
        """
        Returns list of pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests'.format(
            project_id_or_key, repo_id_or_name), method='GET')

    def get_version_milestone_list(self, project_id_or_key):
        """
        Returns list of Versions/Milestones in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/versions'.format(project_id_or_key), method='GET')

    def get_webhook(self, project_id_or_key, webhook_id):
        """
        Returns information about webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/webhooks/{}'.format(project_id_or_key, webhook_id), method='GET')

    def update_category_raw(self, _id, project_id_or_key, form_parameters):
        """
        Updates information about Category.

        :param int _id: Category ID
        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/categories/{}'.format(
            _id, project_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_category(self, _id, project_id_or_key, name=None):
        """
        Updates information about Category.

        :param int _id: Category ID
        :param str project_id_or_key: Project ID or Project Key
        :param str name: Category name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name
        }

        return self._request('/projects/{}/categories/{}'.format(
            _id, project_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_custom_field_raw(self, _id, project_id_or_key, form_parameters):
        """
        Updates Custom Field.

        :param int _id: Custom Field ID
        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/customFields/{}'.format(
            _id, project_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_custom_field(self, _id, project_id_or_key, name,
                            applicable_issue_types=None, description=None, required=None):
        """
        Updates Custom Field.

        :param int _id: Custom Field ID
        :param str project_id_or_key: Project ID or Project Key
        :param list[int] or int applicable_issue_types: Type ID to enable Custom fields
        :param str description: Description
        :param str name: Name
        :param bool required: True to make the Custom field required

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'applicableIssueTypes[]': applicable_issue_types,
            'description': description,
            'name': name,
            'required': self._bool_to_str(required)
        }

        return self._request('/projects/{}/customFields/{}'.format(
            _id, project_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_issue_type_raw(self, _id, project_id_or_key, form_parameters):
        """
        Updates information about Issue Type.

        :param int _id: Issue Type ID
        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/issueTypes/{}'.format(
            _id, project_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_issue_type(self, _id, project_id_or_key, color=None, name=None):
        """
        Updates information about Issue Type.

        :param int _id: Issue Type ID
        :param str project_id_or_key: Project ID or Project Key
        :param str color: Background color : available
        :param str name: Issue Type Name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'color': color,
            'name': name
        }

        return self._request('/projects/{}/issueTypes/{}'.format(
            _id, project_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_list_item_for_list_type_custom_field(
            self, _id, item_id, project_id_or_key):
        """
        Updates list item for list type custom field. Calling API fails if specified custom field’s type is not a list.

        :param int _id: Custom field ID
        :param int item_id: List item ID
        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/customFields/{}/items/{}'.format(
            _id, item_id, project_id_or_key), method='PATCH')

    def update_project_raw(self, project_id_or_key, form_parameters):
        """
        Updates information about project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}'.format(project_id_or_key),
                             method='PATCH', form_parameters=form_parameters)

    def update_project(self, project_id_or_key, archived=None, chart_enabled=None, key=None, name=None,
                       project_leader_can_edit_project_leader=None, subtasking_enabled=None, text_formatting_rule=None):
        """
        Updates information about project.

        :param str project_id_or_key: Project ID or Project Key
        :param bool archived: archive
        :param bool chart_enabled: Enable chart
        :param str key: Project Key
        :param str name: Project Name
        :param bool project_leader_can_edit_project_leader: Allow project administrators to manage each other
        :param bool subtasking_enabled: Enable subtasking
        :param str text_formatting_rule: Formatting rules “backlog” or “markdown”

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'archived': self._bool_to_str(archived),
            'chartEnabled': self._bool_to_str(chart_enabled),
            'key': key,
            'name': name,
            'projectLeaderCanEditProjectLeader': self._bool_to_str(project_leader_can_edit_project_leader),
            'subtaskingEnabled': self._bool_to_str(subtasking_enabled),
            'textFormattingRule': text_formatting_rule
        }

        return self._request('/projects/{}'.format(project_id_or_key),
                             method='PATCH', form_parameters=form_parameters)

    def update_pull_request_raw(
            self, number, project_id_or_key, repo_id_or_name, form_parameters):
        """
        Updates pull requests.

        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}'.format(
            number, project_id_or_key, repo_id_or_name), method='PATCH', form_parameters=form_parameters)

    def update_pull_request(self, number, project_id_or_key, repo_id_or_name, assignee_id=None,
                            comment=None, description=None, issue_id=None, notified_user_id=None, summary=None):
        """
        Updates pull requests.

        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int assignee_id: Assignee’s ID of pull request
        :param str comment: Comment
        :param str description: Description of pull request
        :param int issue_id: Related issue’s ID
        :param list[int] or int notified_user_id: User ID to send notification when pull request is added
        :param str summary: Summary of pull request

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'assigneeId': assignee_id,
            'comment': comment,
            'description': description,
            'issueId': issue_id,
            'notifiedUserId[]': notified_user_id,
            'summary': summary
        }

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}'.format(
            number, project_id_or_key, repo_id_or_name), method='PATCH', form_parameters=form_parameters)

    def update_pull_request_comment_information_raw(
            self, comment_id, number, project_id_or_key, repo_id_or_name, form_parameters):
        """
        Updates pull request comment information.

        :param int comment_id: Comment’s ID
        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments/{}'.format(
            comment_id, number, project_id_or_key, repo_id_or_name), method='PATCH', form_parameters=form_parameters)

    def update_pull_request_comment_information(
            self, comment_id, number, project_id_or_key, repo_id_or_name, content=None):
        """
        Updates pull request comment information.

        :param int comment_id: Comment’s ID
        :param int number: Pull request number
        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param str content: Comment’s body

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'content': content
        }

        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments/{}'.format(
            comment_id, number, project_id_or_key, repo_id_or_name), method='PATCH', form_parameters=form_parameters)

    def update_version_milestone_raw(
            self, _id, project_id_or_key, form_parameters):
        """
        Updates information about Version/Milestone.

        :param int _id: Version ID
        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/versions/{}'.format(
            _id, project_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_version_milestone(self, _id, project_id_or_key, name, archived=None,
                                 description=None, release_due_date=None, start_date=None):
        """
        Updates information about Version/Milestone.

        :param int _id: Version ID
        :param str project_id_or_key: Project ID or Project Key
        :param bool archived: archived
        :param str description: Version Description
        :param str name: Version Name
        :param str release_due_date: Release Due Date
        :param str start_date: Start Date

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'archived': self._bool_to_str(archived),
            'description': description,
            'name': name,
            'releaseDueDate': release_due_date,
            'startDate': start_date
        }

        return self._request('/projects/{}/versions/{}'.format(
            _id, project_id_or_key), method='PATCH', form_parameters=form_parameters)

    def update_webhook_raw(self, project_id_or_key,
                           webhook_id, form_parameters):
        """
        Updates information about webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/projects/{}/webhooks/{}'.format(project_id_or_key,
                                                               webhook_id), method='PATCH', form_parameters=form_parameters)

    def update_webhook(self, project_id_or_key, webhook_id, activity_type_ids=None,
                       all_event=None, description=None, hook_url=None, name=None):
        """
        Updates information about webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID
        :param list[int] or int activity_type_ids: Event ID to be notified
        :param bool all_event: True to make all events notified
        :param str description: Description
        :param str hook_url: hook URL
        :param str name: Name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'activityTypeIds[]': activity_type_ids,
            'allEvent': self._bool_to_str(all_event),
            'description': description,
            'hookUrl': hook_url,
            'name': name
        }

        return self._request('/projects/{}/webhooks/{}'.format(project_id_or_key,
                                                               webhook_id), method='PATCH', form_parameters=form_parameters)
