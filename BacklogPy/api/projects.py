# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase, SUFFIX_JP


class Projects(BacklogBase):
    def __init__(self, space_id, api_key, suffix=SUFFIX_JP):
        super(Projects, self).__init__(space_id, api_key, suffix=suffix)

    def add_category_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Category to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/categories'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

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

        return self._request(
            '/projects/{}/categories'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_custom_field_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Custom Field to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_custom_field(
            self,
            project_id_or_key,
            type_id,
            name,
            applicable_issue_types=None,
            description=None,
            required=None):
        """
        Adds new Custom Field to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param int type_id: Type ID of Custom field
        :param str name: Name
        :param list[int] or int or None applicable_issue_types: Type ID to enable Custom fields
        :param str or None description: Description
        :param bool or None required: True to make the Custom field required

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'typeId': type_id,
            'name': name,
            'applicableIssueTypes[]': applicable_issue_types,
            'description': description,
            'required': self._bool_to_str(required)
        }

        return self._request(
            '/projects/{}/customFields'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_issue_type_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Issue Type to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/issueTypes'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_issue_type(
            self,
            project_id_or_key,
            name,
            color,
            template_summary=None,
            template_description=None):
        """
        Adds new Issue Type to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param str name: Issue Type name
        :param str color: Background color
        :param str or None template_summary: Subject
        :param str or None template_description: Description

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'color': color,
            'templateSummary': template_summary,
            'templateDescription': template_description
        }

        return self._request(
            '/projects/{}/issueTypes'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_list_item_for_list_type_custom_field_raw(
            self, project_id_or_key, _id, form_parameters):
        """
        Adds new list item for list type custom field. Only administrator can call this API if the option “Add items in adding or editing issues” is disabled in settings. Calling API fails if specified custom field’s type is not a list.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields/{}/items'.format(
                project_id_or_key,
                _id),
            method='POST',
            form_parameters=form_parameters)

    def add_list_item_for_list_type_custom_field(
            self, project_id_or_key, _id, name=None):
        """
        Adds new list item for list type custom field. Only administrator can call this API if the option “Add items in adding or editing issues” is disabled in settings. Calling API fails if specified custom field’s type is not a list.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID
        :param str or None name: List item name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name
        }

        return self._request(
            '/projects/{}/customFields/{}/items'.format(
                project_id_or_key,
                _id),
            method='POST',
            form_parameters=form_parameters)

    def add_project_raw(self, form_parameters):
        """
        Adds new project.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects',
            method='POST',
            form_parameters=form_parameters)

    def add_project(
            self,
            name,
            key,
            chart_enabled=None,
            project_leader_can_edit_project_leader=None,
            subtasking_enabled=None,
            text_formatting_rule=None):
        """
        Adds new project.

        :param str name: Project Name
        :param str key: Project Key (Uppercase letters (A-Z), numbers (0-9) and underscore (_) can be used.)
        :param bool or None chart_enabled: Enable chart
        :param bool or None project_leader_can_edit_project_leader: Allow project administrators to manage each other
        :param bool or None subtasking_enabled: Enable subtasking
        :param str or None text_formatting_rule: Formatting rules “backlog” or “markdown”

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'key': key,
            'chartEnabled': self._bool_to_str(chart_enabled),
            'projectLeaderCanEditProjectLeader': self._bool_to_str(project_leader_can_edit_project_leader),
            'subtaskingEnabled': self._bool_to_str(subtasking_enabled),
            'textFormattingRule': text_formatting_rule}

        return self._request(
            '/projects',
            method='POST',
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

        return self._request(
            '/projects/{}/administrators'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_project_administrator(self, project_id_or_key, user_id=None):
        """
        Adds “Project Administrator” role to user

        :param str project_id_or_key: Project ID or Project Key
        :param int or None user_id: User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'userId': user_id
        }

        return self._request(
            '/projects/{}/administrators'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_project_group_raw(self, project_id_or_key, form_parameters):
        """
        Add group to project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/groups'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_project_group(self, project_id_or_key, group_id=None):
        """
        Add group to project.

        :param str project_id_or_key: Project ID or Project Key
        :param int or None group_id: Group ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'groupId': group_id
        }

        return self._request(
            '/projects/{}/groups'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_project_team_raw(self, project_id_or_key, form_parameters):
        """
        Add team to project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/teams'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_project_team(self, project_id_or_key, team_id=None):
        """
        Add team to project.

        :param str project_id_or_key: Project ID or Project Key
        :param int or None team_id: Team ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'teamId': team_id
        }

        return self._request(
            '/projects/{}/teams'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_project_user_raw(self, project_id_or_key, form_parameters):
        """
        Adds user to list of project members.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/users'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_project_user(self, project_id_or_key, user_id=None):
        """
        Adds user to list of project members.

        :param str project_id_or_key: Project ID or Project Key
        :param int or None user_id: User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'userId': user_id
        }

        return self._request(
            '/projects/{}/users'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_pull_request_raw(
            self,
            project_id_or_key,
            repo_id_or_name,
            form_parameters):
        """
        Adds pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests'.format(
                project_id_or_key,
                repo_id_or_name),
            method='POST',
            form_parameters=form_parameters)

    def add_pull_request(
            self,
            project_id_or_key,
            repo_id_or_name,
            summary,
            description,
            base,
            branch,
            issue_id=None,
            assignee_id=None,
            notified_user_id=None,
            attachment_id=None):
        """
        Adds pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param str summary: Summary of pull request
        :param str description: Description of pull request
        :param str base: Branch name of merge base
        :param str branch: Name of merging branch
        :param int or None issue_id: Related issue’s ID
        :param int or None assignee_id: Assignee’s ID of pull request
        :param list[int] or int or None notified_user_id: User ID to send notification when pull request is added
        :param list[int] or int or None attachment_id: ID returned by “Post Attachment File” API

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'summary': summary,
            'description': description,
            'base': base,
            'branch': branch,
            'issueId': issue_id,
            'assigneeId': assignee_id,
            'notifiedUserId[]': notified_user_id,
            'attachmentId[]': attachment_id
        }

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests'.format(
                project_id_or_key,
                repo_id_or_name),
            method='POST',
            form_parameters=form_parameters)

    def add_pull_request_comment_raw(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            form_parameters):
        """
        Adds comments on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
                project_id_or_key,
                repo_id_or_name,
                number),
            method='POST',
            form_parameters=form_parameters)

    def add_pull_request_comment(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            content,
            attachment_id=None,
            notified_user_id=None):
        """
        Adds comments on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param str content: Comment
        :param list[int] or int or None attachment_id: Attachment file ID(Post Attachment File returns)
        :param list[int] or int or None notified_user_id: User ID to send notification when comment is added

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'content': content,
            'attachmentId[]': attachment_id,
            'notifiedUserId[]': notified_user_id
        }

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
                project_id_or_key,
                repo_id_or_name,
                number),
            method='POST',
            form_parameters=form_parameters)

    def add_status_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Status to the project. You can create up to 8 custom statuses within a Project aside from the 4 default.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/statuses'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_status(self, project_id_or_key, name, color):
        """
        Adds new Status to the project. You can create up to 8 custom statuses within a Project aside from the 4 default.

        :param str project_id_or_key: Project ID or Project Key
        :param str name: Status name
        :param str color: Background color: You can use the below colors

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'color': color
        }

        return self._request(
            '/projects/{}/statuses'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_version_milestone_raw(self, project_id_or_key, form_parameters):
        """
        Adds new Version/Milestone to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/versions'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_version_milestone(
            self,
            project_id_or_key,
            name,
            description=None,
            start_date=None,
            release_due_date=None):
        """
        Adds new Version/Milestone to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param str name: Version name
        :param str or None description: Version description
        :param str or None start_date: Start Date (yyyy-MM-dd)
        :param str or None release_due_date: End Date (yyyy-MM-dd)

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'description': description,
            'startDate': start_date,
            'releaseDueDate': release_due_date
        }

        return self._request(
            '/projects/{}/versions'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_webhook_raw(self, project_id_or_key, form_parameters):
        """
        Adds new webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/webhooks'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def add_webhook(
            self,
            project_id_or_key,
            name=None,
            description=None,
            hook_url=None,
            all_event=None,
            activity_type_ids=None):
        """
        Adds new webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str or None name: Name
        :param str or None description: Description
        :param str or None hook_url: hook URL
        :param bool or None all_event: True to make all events notified
        :param list[int] or int or None activity_type_ids: Event ID to be notified

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'description': description,
            'hookUrl': hook_url,
            'allEvent': self._bool_to_str(all_event),
            'activityTypeIds[]': activity_type_ids
        }

        return self._request(
            '/projects/{}/webhooks'.format(project_id_or_key),
            method='POST',
            form_parameters=form_parameters)

    def delete_category(self, project_id_or_key, _id):
        """
        Deletes Category.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Category ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/categories/{}'.format(project_id_or_key, _id), method='DELETE')

    def delete_custom_field(self, project_id_or_key, _id):
        """
        Deletes Custom Field.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields/{}'.format(project_id_or_key, _id), method='DELETE')

    def delete_issue_type_raw(self, project_id_or_key, _id, form_parameters):
        """
        Deletes Issue Type.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Issue Type ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/issueTypes/{}'.format(
                project_id_or_key,
                _id),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_issue_type(
            self,
            project_id_or_key,
            _id,
            substitute_issue_type_id):
        """
        Deletes Issue Type.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Issue Type ID
        :param int substitute_issue_type_id: type ID to change linked issue

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'substituteIssueTypeId': substitute_issue_type_id
        }

        return self._request(
            '/projects/{}/issueTypes/{}'.format(
                project_id_or_key,
                _id),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_list_item_for_list_type_custom_field(
            self, project_id_or_key, _id, item_id):
        """
        Deletes list item for list type custom field. Calling API fails if specified custom field’s type is not a list.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID
        :param int item_id: List item ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields/{}/items/{}'.format(
                project_id_or_key, _id, item_id), method='DELETE')

    def delete_project(self, project_id_or_key):
        """
        Deletes project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}'.format(project_id_or_key),
            method='DELETE')

    def delete_project_administrator_raw(
            self, project_id_or_key, form_parameters):
        """
        Removes Project Administrator role from user

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/administrators'.format(project_id_or_key),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_project_administrator(self, project_id_or_key, user_id=None):
        """
        Removes Project Administrator role from user

        :param str project_id_or_key: Project ID or Project Key
        :param int or None user_id: User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'userId': user_id
        }

        return self._request(
            '/projects/{}/administrators'.format(project_id_or_key),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_project_group_raw(self, project_id_or_key, form_parameters):
        """
        Removes a group from the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/groups'.format(project_id_or_key),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_project_group(self, project_id_or_key, group_id=None):
        """
        Removes a group from the project.

        :param str project_id_or_key: Project ID or Project Key
        :param int or None group_id: Group ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'groupId': group_id
        }

        return self._request(
            '/projects/{}/groups'.format(project_id_or_key),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_project_team_raw(self, project_id_or_key, form_parameters):
        """
        Removes a team from the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/teams'.format(project_id_or_key),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_project_team(self, project_id_or_key, team_id=None):
        """
        Removes a team from the project.

        :param str project_id_or_key: Project ID or Project Key
        :param int or None team_id: Team ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'teamId': team_id
        }

        return self._request(
            '/projects/{}/teams'.format(project_id_or_key),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_project_user_raw(self, project_id_or_key, form_parameters):
        """
        Removes user from list project members.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/users'.format(project_id_or_key),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_project_user(self, project_id_or_key, user_id=None):
        """
        Removes user from list project members.

        :param str project_id_or_key: Project ID or Project Key
        :param int or None user_id: User ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'userId': user_id
        }

        return self._request(
            '/projects/{}/users'.format(project_id_or_key),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_pull_request_attachments(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            attachment_id):
        """
        Deletes attached files on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param int attachment_id: Attached file’s ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/attachments/{}'.format(
                project_id_or_key,
                repo_id_or_name,
                number,
                attachment_id),
            method='DELETE')

    def delete_status_raw(self, project_id_or_key, _id, form_parameters):
        """
        Deletes Status.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Status ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/statuses/{}'.format(
                project_id_or_key,
                _id),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_status(self, project_id_or_key, _id, substitute_status_id):
        """
        Deletes Status.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Status ID
        :param int substitute_status_id: Status ID to replace linked issues statuses.

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'substituteStatusId': substitute_status_id
        }

        return self._request(
            '/projects/{}/statuses/{}'.format(
                project_id_or_key,
                _id),
            method='DELETE',
            form_parameters=form_parameters)

    def delete_version(self, project_id_or_key, _id):
        """
        Deletes Version.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Version のID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/versions/{}'.format(project_id_or_key, _id), method='DELETE')

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
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            attachment_id):
        """
        Downloads attached files on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param int attachment_id: Attached file’s ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/attachments/{}'.format(
                project_id_or_key,
                repo_id_or_name,
                number,
                attachment_id),
            method='GET')

    def get_category_list(self, project_id_or_key):
        """
        Returns list of Categories in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/categories'.format(project_id_or_key),
            method='GET')

    def get_custom_field_list(self, project_id_or_key):
        """
        Returns list of Custom Fields in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields'.format(project_id_or_key),
            method='GET')

    def get_file(self, project_id_or_key, shared_file_id):
        """
        Downloads the file.

        :param str project_id_or_key: Project ID or Project Key
        :param int shared_file_id: File ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/files/{}'.format(project_id_or_key, shared_file_id), method='GET')

    def get_git_repository(self, project_id_or_key, repo_id_or_name):
        """
        Returns Git repository.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}'.format(
                project_id_or_key,
                repo_id_or_name),
            method='GET')

    def get_issue_type_list(self, project_id_or_key):
        """
        Returns list of Issue Types in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/issueTypes'.format(project_id_or_key),
            method='GET')

    def get_list_of_git_repositories(self, project_id_or_key):
        """
        Returns list of Git repositories.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories'.format(project_id_or_key),
            method='GET')

    def get_list_of_project_administrators(self, project_id_or_key):
        """
        Returns list of users who has Project Administrator role

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/administrators'.format(project_id_or_key),
            method='GET')

    def get_list_of_pull_request_attachment(
            self, project_id_or_key, repo_id_or_name, number):
        """
        Returns list of attached files on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/attachments'.format(
                project_id_or_key, repo_id_or_name, number), method='GET')

    def get_list_of_shared_files_raw(
            self,
            project_id_or_key,
            path,
            query_parameters):
        """
        Gets list of Shared Files.

        :param str project_id_or_key: Project ID or Project key
        :param str path: Directory path
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/files/metadata/{}'.format(
                project_id_or_key,
                path),
            method='GET',
            query_parameters=query_parameters)

    def get_list_of_shared_files(
            self,
            project_id_or_key,
            path,
            order=None,
            offset=None,
            count=None):
        """
        Gets list of Shared Files.

        :param str project_id_or_key: Project ID or Project key
        :param str path: Directory path
        :param str or None order: “asc” or “desc” default=“desc”
        :param int or None offset: offset
        :param int or None count: number of records to retrieve(1-100) default=20

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'order': order,
            'offset': offset,
            'count': count
        }

        return self._request(
            '/projects/{}/files/metadata/{}'.format(
                project_id_or_key,
                path),
            method='GET',
            query_parameters=query_parameters)

    def get_list_of_webhooks(self, project_id_or_key):
        """
        Returns list of webhooks.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/webhooks'.format(project_id_or_key),
            method='GET')

    def get_number_of_pull_request_comments(
            self, project_id_or_key, repo_id_or_name, number):
        """
        Returns number of comments on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/comments/count'.format(
                project_id_or_key, repo_id_or_name, number), method='GET')

    def get_number_of_pull_requests_raw(
            self,
            project_id_or_key,
            repo_id_or_name,
            query_parameters):
        """
        Returns number of pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/count'.format(
                project_id_or_key,
                repo_id_or_name),
            method='GET',
            query_parameters=query_parameters)

    def get_number_of_pull_requests(
            self,
            project_id_or_key,
            repo_id_or_name,
            status_id=None,
            assignee_id=None,
            issue_id=None,
            created_user_id=None,
            offset=None,
            count=None):
        """
        Returns number of pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param list[int] or int or None status_id: Status ID
        :param list[int] or int or None assignee_id: Assignee ID
        :param list[int] or int or None issue_id: Related issue ID
        :param list[int] or int or None created_user_id: Created User ID
        :param int or None offset: offset
        :param int or None count: number of records to retrieve(1-100) default=20

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'statusId[]': status_id,
            'assigneeId[]': assignee_id,
            'issueId[]': issue_id,
            'createdUserId[]': created_user_id,
            'offset': offset,
            'count': count
        }

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/count'.format(
                project_id_or_key,
                repo_id_or_name),
            method='GET',
            query_parameters=query_parameters)

    def get_project(self, project_id_or_key):
        """
        Returns information about project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}'.format(project_id_or_key),
            method='GET')

    def get_project_disk_usage(self, project_id_or_key):
        """
        Returns information about project disk usage.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/diskUsage'.format(project_id_or_key),
            method='GET')

    def get_project_group_list(self, project_id_or_key):
        """
        Returns list of project groups.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/groups'.format(project_id_or_key),
            method='GET')

    def get_project_icon(self, project_id_or_key):
        """
        Downloads project icon.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/image'.format(project_id_or_key),
            method='GET')

    def get_project_list_raw(self, query_parameters):
        """
        Returns list of projects.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects',
            method='GET',
            query_parameters=query_parameters)

    def get_project_list(self, archived=None, all=None):
        """
        Returns list of projects.

        :param bool or None archived: For unspecified parameters, this form returns all projects. For ‘false’ parameters, it returns unarchived projects. For ‘true’ parameters, it returns archived projects.
        :param bool or None all: Only applies to administrators. If ‘true,’ it returns all projects. If ‘false,’ it returns only projects they have joined (set to ‘false’ by default).

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'archived': self._bool_to_str(archived),
            'all': self._bool_to_str(all)
        }

        return self._request(
            '/projects',
            method='GET',
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

        return self._request(
            '/projects/{}/activities'.format(project_id_or_key),
            method='GET',
            query_parameters=query_parameters)

    def get_project_recent_updates(
            self,
            project_id_or_key,
            activity_type_id=None,
            min_id=None,
            max_id=None,
            count=None,
            order=None):
        """
        Returns recent update in the project.

        :param str project_id_or_key: Project ID or Project Key
        :param list[int] or int or None activity_type_id: type(1-26)
        :param int or None min_id: minimum ID
        :param int or None max_id: maximum ID
        :param int or None count: number of records to retrieve(1-100) default=20
        :param str or None order: “asc” or “desc” default=“desc”

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'activityTypeId[]': activity_type_id,
            'minId': min_id,
            'maxId': max_id,
            'count': count,
            'order': order
        }

        return self._request(
            '/projects/{}/activities'.format(project_id_or_key),
            method='GET',
            query_parameters=query_parameters)

    def get_project_team_list(self, project_id_or_key):
        """
        Returns list of project teams.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/teams'.format(project_id_or_key),
            method='GET')

    def get_project_user_list_raw(self, project_id_or_key, query_parameters):
        """
        Returns list of project members.

        :param str project_id_or_key: Project ID or Project Key
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/users'.format(project_id_or_key),
            method='GET',
            query_parameters=query_parameters)

    def get_project_user_list(
            self,
            project_id_or_key,
            exclude_group_members=None):
        """
        Returns list of project members.

        :param str project_id_or_key: Project ID or Project Key
        :param bool or None exclude_group_members: Set to true to exclude members that part of project groups and false to get all members. Default is false.

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'excludeGroupMembers': self._bool_to_str(exclude_group_members)
        }

        return self._request(
            '/projects/{}/users'.format(project_id_or_key),
            method='GET',
            query_parameters=query_parameters)

    def get_pull_request(self, project_id_or_key, repo_id_or_name, number):
        """
        Returns pull reuqest.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}'.format(
                project_id_or_key,
                repo_id_or_name,
                number),
            method='GET')

    def get_pull_request_comment_raw(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            query_parameters):
        """
        Returns list of pull request comments.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
                project_id_or_key,
                repo_id_or_name,
                number),
            method='GET',
            query_parameters=query_parameters)

    def get_pull_request_comment(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            min_id=None,
            max_id=None,
            count=None,
            order=None):
        """
        Returns list of pull request comments.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param int or None min_id: minimum ID
        :param int or None max_id: maximum ID
        :param int or None count: number of records to retrieve(1-100) default=20
        :param str or None order: “asc” or “desc” default=“desc”

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
            '/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
                project_id_or_key,
                repo_id_or_name,
                number),
            method='GET',
            query_parameters=query_parameters)

    def get_pull_request_list_raw(
            self,
            project_id_or_key,
            repo_id_or_name,
            query_parameters):
        """
        Returns list of pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests'.format(
                project_id_or_key,
                repo_id_or_name),
            method='GET',
            query_parameters=query_parameters)

    def get_pull_request_list(
            self,
            project_id_or_key,
            repo_id_or_name,
            status_id=None,
            assignee_id=None,
            issue_id=None,
            created_user_id=None,
            offset=None,
            count=None):
        """
        Returns list of pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param list[int] or int or None status_id: Status ID
        :param list[int] or int or None assignee_id: Assignee ID
        :param list[int] or int or None issue_id: Issue ID
        :param list[int] or int or None created_user_id: Created User ID
        :param int or None offset: offset
        :param int or None count: number of records to retrieve(1-100) default=20

        :return:  requests Response object
        :rtype: requests.Response
        """

        query_parameters = {
            'statusId[]': status_id,
            'assigneeId[]': assignee_id,
            'issueId[]': issue_id,
            'createdUserId[]': created_user_id,
            'offset': offset,
            'count': count
        }

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests'.format(
                project_id_or_key,
                repo_id_or_name),
            method='GET',
            query_parameters=query_parameters)

    def get_status_list_of_project(self, project_id_or_key):
        """
        Returns list of status in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/statuses'.format(project_id_or_key),
            method='GET')

    def get_version_milestone_list(self, project_id_or_key):
        """
        Returns list of Versions/Milestones in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/versions'.format(project_id_or_key),
            method='GET')

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

    def update_category_raw(self, project_id_or_key, _id, form_parameters):
        """
        Updates information about Category.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Category ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/categories/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_category(self, project_id_or_key, _id, name=None):
        """
        Updates information about Category.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Category ID
        :param str or None name: Category name

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name
        }

        return self._request(
            '/projects/{}/categories/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_custom_field_raw(self, project_id_or_key, _id, form_parameters):
        """
        Updates Custom Field.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom Field ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_custom_field(
            self,
            project_id_or_key,
            _id,
            name=None,
            applicable_issue_types=None,
            description=None,
            required=None):
        """
        Updates Custom Field.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom Field ID
        :param str or None name: Name
        :param list[int] or int or None applicable_issue_types: Type ID to enable Custom fields
        :param str or None description: Description
        :param bool or None required: True to make the Custom field required

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'applicableIssueTypes[]': applicable_issue_types,
            'description': description,
            'required': self._bool_to_str(required)
        }

        return self._request(
            '/projects/{}/customFields/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_issue_type_raw(self, project_id_or_key, _id, form_parameters):
        """
        Updates information about Issue Type.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Issue Type ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/issueTypes/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_issue_type(
            self,
            project_id_or_key,
            _id,
            name=None,
            color=None,
            template_summary=None,
            template_description=None):
        """
        Updates information about Issue Type.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Issue Type ID
        :param str or None name: Issue Type Name
        :param str or None color: Background color : available
        :param str or None template_summary: Subject
        :param str or None template_description: Description

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'color': color,
            'templateSummary': template_summary,
            'templateDescription': template_description
        }

        return self._request(
            '/projects/{}/issueTypes/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_list_item_for_list_type_custom_field_raw(
            self, project_id_or_key, _id, item_id, form_parameters):
        """
        Updates list item for list type custom field. Calling API fails if specified custom field’s type is not a list.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID
        :param int item_id: List item ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/customFields/{}/items/{}'.format(
                project_id_or_key,
                _id,
                item_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_list_item_for_list_type_custom_field(
            self, project_id_or_key, _id, item_id, name=None):
        """
        Updates list item for list type custom field. Calling API fails if specified custom field’s type is not a list.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID
        :param int item_id: List item ID
        :param str or None name: Name of list item

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name
        }

        return self._request(
            '/projects/{}/customFields/{}/items/{}'.format(
                project_id_or_key,
                _id,
                item_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_order_of_status_raw(self, project_id_or_key, form_parameters):
        """
        Updates order about Status.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/statuses/updateDisplayOrder'.format(project_id_or_key),
            method='PATCH',
            form_parameters=form_parameters)

    def update_order_of_status(self, project_id_or_key, status_id=None):
        """
        Updates order about Status.

        :param str project_id_or_key: Project ID or Project Key
        :param list[int] or int or None status_id: Status ID List to order them. You have to send all status of project. It has following restrictions as below.

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'statusId[]': status_id
        }

        return self._request(
            '/projects/{}/statuses/updateDisplayOrder'.format(project_id_or_key),
            method='PATCH',
            form_parameters=form_parameters)

    def update_project_raw(self, project_id_or_key, form_parameters):
        """
        Updates information about project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}'.format(project_id_or_key),
            method='PATCH',
            form_parameters=form_parameters)

    def update_project(
            self,
            project_id_or_key,
            name=None,
            key=None,
            chart_enabled=None,
            subtasking_enabled=None,
            project_leader_can_edit_project_leader=None,
            text_formatting_rule=None,
            archived=None):
        """
        Updates information about project.

        :param str project_id_or_key: Project ID or Project Key
        :param str or None name: Project Name
        :param str or None key: Project Key
        :param bool or None chart_enabled: Enable chart
        :param bool or None subtasking_enabled: Enable subtasking
        :param bool or None project_leader_can_edit_project_leader: Allow project administrators to manage each other
        :param str or None text_formatting_rule: Formatting rules “backlog” or “markdown”
        :param bool or None archived: archive

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'key': key,
            'chartEnabled': self._bool_to_str(chart_enabled),
            'subtaskingEnabled': self._bool_to_str(subtasking_enabled),
            'projectLeaderCanEditProjectLeader': self._bool_to_str(project_leader_can_edit_project_leader),
            'textFormattingRule': text_formatting_rule,
            'archived': self._bool_to_str(archived)}

        return self._request(
            '/projects/{}'.format(project_id_or_key),
            method='PATCH',
            form_parameters=form_parameters)

    def update_pull_request_raw(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            form_parameters):
        """
        Updates pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}'.format(
                project_id_or_key,
                repo_id_or_name,
                number),
            method='PATCH',
            form_parameters=form_parameters)

    def update_pull_request(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            summary=None,
            description=None,
            issue_id=None,
            assignee_id=None,
            notified_user_id=None,
            comment=None):
        """
        Updates pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param str or None summary: Summary of pull request
        :param str or None description: Description of pull request
        :param int or None issue_id: Related issue’s ID
        :param int or None assignee_id: Assignee’s ID of pull request
        :param list[int] or int or None notified_user_id: User ID to send notification when pull request is added
        :param str or None comment: Comment

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'summary': summary,
            'description': description,
            'issueId': issue_id,
            'assigneeId': assignee_id,
            'notifiedUserId[]': notified_user_id,
            'comment': comment
        }

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}'.format(
                project_id_or_key,
                repo_id_or_name,
                number),
            method='PATCH',
            form_parameters=form_parameters)

    def update_pull_request_comment_information_raw(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            comment_id,
            form_parameters):
        """
        Updates pull request comment information.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param int comment_id: Comment’s ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/comments/{}'.format(
                project_id_or_key,
                repo_id_or_name,
                number,
                comment_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_pull_request_comment_information(
            self,
            project_id_or_key,
            repo_id_or_name,
            number,
            comment_id,
            content=None):
        """
        Updates pull request comment information.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param int comment_id: Comment’s ID
        :param str or None content: Comment’s body

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'content': content
        }

        return self._request(
            '/projects/{}/git/repositories/{}/pullRequests/{}/comments/{}'.format(
                project_id_or_key,
                repo_id_or_name,
                number,
                comment_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_status_raw(self, project_id_or_key, _id, form_parameters):
        """
        Updates information about Status.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Status ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/statuses/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_status(self, project_id_or_key, _id, name=None, color=None):
        """
        Updates information about Status.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Status ID
        :param str or None name: Status Name
        :param str or None color: Background color : available

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'color': color
        }

        return self._request(
            '/projects/{}/statuses/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_version_milestone_raw(
            self, project_id_or_key, _id, form_parameters):
        """
        Updates information about Version/Milestone.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Version ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/versions/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_version_milestone(
            self,
            project_id_or_key,
            _id,
            name,
            description=None,
            start_date=None,
            release_due_date=None,
            archived=None):
        """
        Updates information about Version/Milestone.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Version ID
        :param str name: Version Name
        :param str or None description: Version Description
        :param str or None start_date: Start Date (yyyy-MM-dd)
        :param str or None release_due_date: End Date (yyyy-MM-dd)
        :param bool or None archived: archived

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'description': description,
            'startDate': start_date,
            'releaseDueDate': release_due_date,
            'archived': self._bool_to_str(archived)
        }

        return self._request(
            '/projects/{}/versions/{}'.format(
                project_id_or_key,
                _id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_webhook_raw(
            self,
            project_id_or_key,
            webhook_id,
            form_parameters):
        """
        Updates information about webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/projects/{}/webhooks/{}'.format(
                project_id_or_key,
                webhook_id),
            method='PATCH',
            form_parameters=form_parameters)

    def update_webhook(
            self,
            project_id_or_key,
            webhook_id,
            name=None,
            description=None,
            hook_url=None,
            all_event=None,
            activity_type_ids=None):
        """
        Updates information about webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID
        :param str or None name: Name
        :param str or None description: Description
        :param str or None hook_url: hook URL
        :param bool or None all_event: True to make all events notified
        :param list[int] or int or None activity_type_ids: Event ID to be notified

        :return:  requests Response object
        :rtype: requests.Response
        """

        form_parameters = {
            'name': name,
            'description': description,
            'hookUrl': hook_url,
            'allEvent': self._bool_to_str(all_event),
            'activityTypeIds[]': activity_type_ids
        }

        return self._request(
            '/projects/{}/webhooks/{}'.format(
                project_id_or_key,
                webhook_id),
            method='PATCH',
            form_parameters=form_parameters)
