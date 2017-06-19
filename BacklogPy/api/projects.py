# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Projects(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Projects, self).__init__(space_id, api_key)

    def add_category(self, project_id_or_key, form_parameters):
        """
        Adds new Category to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/categories'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_custom_field(self, project_id_or_key, form_parameters):
        """
        Adds new Custom Field to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/customFields'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_issue_type(self, project_id_or_key, form_parameters):
        """
        Adds new Issue Type to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/issueTypes'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_list_item_for_list_type_custom_field(
            self, project_id_or_key, _id, form_parameters):
        """
        Adds new list item for list type custom field. Only administrator can call this API if the option “Add items in adding or editing issues” is disabled in settings. Calling API fails if specified custom field’s type is not a list.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/customFields/{}/items'.format(
            project_id_or_key, _id), method='POST', form_parameters=form_parameters)

    def add_project_administrator(self, project_id_or_key, form_parameters):
        """
        Adds “Project Administrator” role to user

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/administrators'.format(
            project_id_or_key), method='POST', form_parameters=form_parameters)

    def add_project_user(self, project_id_or_key, form_parameters):
        """
        Adds user to list of project members.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/users'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_project(self, form_parameters):
        """
        Adds new project.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects', method='POST',
                             form_parameters=form_parameters)

    def add_pull_request_comment(
            self, project_id_or_key, repo_id_or_name, number, form_parameters):
        """
        Adds comments on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
            project_id_or_key, repo_id_or_name, number), method='POST', form_parameters=form_parameters)

    def add_pull_request(self, project_id_or_key,
                         repo_id_or_name, form_parameters):
        """
        Adds pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests'.format(
            project_id_or_key, repo_id_or_name), method='POST', form_parameters=form_parameters)

    def add_version_milestone(self, project_id_or_key, form_parameters):
        """
        Adds new Version/Milestone to the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/versions'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def add_webhook(self, project_id_or_key, form_parameters):
        """
        Adds new webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/webhooks'.format(project_id_or_key),
                             method='POST', form_parameters=form_parameters)

    def delete_category(self, project_id_or_key, _id):
        """
        Deletes Category.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Category ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/categories/{}'.format(project_id_or_key, _id), method='DELETE')

    def delete_custom_field(self, project_id_or_key, _id):
        """
        Deletes Custom Field.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/customFields/{}'.format(project_id_or_key, _id), method='DELETE')

    def delete_issue_type(self, project_id_or_key, _id, form_parameters):
        """
        Deletes Issue Type.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Issue Type ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/issueTypes/{}'.format(
            project_id_or_key, _id), method='DELETE', form_parameters=form_parameters)

    def delete_list_item_for_list_type_custom_field(
            self, project_id_or_key, _id, item_id):
        """
        Deletes list item for list type custom field. Calling API fails if specified custom field’s type is not a list.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID
        :param int item_id: List item ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/customFields/{}/items/{}'.format(
            project_id_or_key, _id, item_id), method='DELETE')

    def delete_project_administrator(self, project_id_or_key, form_parameters):
        """
        Removes Project Administrator role from user

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/administrators'.format(
            project_id_or_key), method='DELETE', form_parameters=form_parameters)

    def delete_project_user(self, project_id_or_key, form_parameters):
        """
        Removes user from list project members.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/users'.format(project_id_or_key),
                             method='DELETE', form_parameters=form_parameters)

    def delete_project(self, project_id_or_key):
        """
        Deletes project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}'.format(project_id_or_key), method='DELETE')

    def delete_pull_request_attachments(
            self, project_id_or_key, repo_id_or_name, number, attachment_id):
        """
        Deletes attached files on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param int attachment_id: Attached file’s ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/attachments/{}'.format(
            project_id_or_key, repo_id_or_name, number, attachment_id), method='DELETE')

    def delete_version(self, project_id_or_key, _id):
        """
        Deletes Version.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Version のID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/versions/{}'.format(project_id_or_key, _id), method='DELETE')

    def delete_webhook(self, project_id_or_key, webhook_id):
        """
        Deletes webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/webhooks/{}'.format(project_id_or_key, webhook_id), method='DELETE')

    def download_pull_request_attachment(
            self, project_id_or_key, repo_id_or_name, number, attachment_id):
        """
        Downloads attached files on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param int attachment_id: Attached file’s ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/attachments/{}'.format(
            project_id_or_key, repo_id_or_name, number, attachment_id), method='GET')

    def get_category_list(self, project_id_or_key):
        """
        Returns list of Categories in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/categories'.format(project_id_or_key), method='GET')

    def get_custom_field_list(self, project_id_or_key):
        """
        Returns list of Custom Fields in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/customFields'.format(project_id_or_key), method='GET')

    def get_file(self, project_id_or_key, _id):
        """
        Downloads the file.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: File ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/files/{}'.format(project_id_or_key, _id), method='GET')

    def get_git_repository(self, project_id_or_key, repo_id_or_name):
        """
        Returns Git repository.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/git/repositories/{}'.format(project_id_or_key, repo_id_or_name), method='GET')

    def get_issue_type_list(self, project_id_or_key):
        """
        Returns list of Issue Types in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/issueTypes'.format(project_id_or_key), method='GET')

    def get_list_of_git_repositories(self, project_id_or_key):
        """
        Returns list of Git repositories.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/git/repositories'.format(project_id_or_key), method='GET')

    def get_list_of_project_administrators(self, project_id_or_key):
        """
        Returns list of users who has Project Administrator role

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/administrators'.format(project_id_or_key), method='GET')

    def get_list_of_pull_request_attachment(
            self, project_id_or_key, repo_id_or_name, number):
        """
        Returns list of attached files on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/attachments'.format(
            project_id_or_key, repo_id_or_name, number), method='GET')

    def get_list_of_shared_files(
            self, project_id_or_key, path, query_parameters):
        """
        Gets list of Shared Files.

        :param str project_id_or_key: Project ID or Project key
        :param str path: Directory path
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/files/metadata/{}'.format(
            project_id_or_key, path), method='GET', query_parameters=query_parameters)

    def get_list_of_webhooks(self, project_id_or_key):
        """
        Returns list of webhooks.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/webhooks'.format(project_id_or_key), method='GET')

    def get_number_of_pull_request_comments(
            self, project_id_or_key, repo_id_or_name, number):
        """
        Returns number of comments on pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments/count'.format(
            project_id_or_key, repo_id_or_name, number), method='GET')

    def get_number_of_pull_requests(self, project_id_or_key, repo_id_or_name):
        """
        Returns number of pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/count'.format(
            project_id_or_key, repo_id_or_name), method='GET')

    def get_project_disk_usage(self, project_id_or_key):
        """
        Returns information about project disk usage.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/diskUsage'.format(project_id_or_key), method='GET')

    def get_project_icon(self, project_id_or_key):
        """
        Downloads project icon.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/image'.format(project_id_or_key), method='GET')

    def get_project_list(self, query_parameters):
        """
        Returns list of projects.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects', method='GET',
                             query_parameters=query_parameters)

    def get_project_recent_updates(self, project_id_or_key, query_parameters):
        """
        Returns recent update in the project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/activities'.format(project_id_or_key),
                             method='GET', query_parameters=query_parameters)

    def get_project_user_list(self, project_id_or_key):
        """
        Returns list of project members.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/users'.format(project_id_or_key), method='GET')

    def get_project(self, project_id_or_key):
        """
        Returns information about project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}'.format(project_id_or_key), method='GET')

    def get_pull_request_comment(
            self, project_id_or_key, repo_id_or_name, number):
        """
        Returns list of pull request comments.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments'.format(
            project_id_or_key, repo_id_or_name, number), method='GET')

    def get_pull_request_list(self, project_id_or_key, repo_id_or_name):
        """
        Returns list of pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests'.format(
            project_id_or_key, repo_id_or_name), method='GET')

    def get_pull_request(self, project_id_or_key, repo_id_or_name, number):
        """
        Returns pull reuqest.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}'.format(
            project_id_or_key, repo_id_or_name, number), method='GET')

    def get_version_milestone_list(self, project_id_or_key):
        """
        Returns list of Versions/Milestones in the project.

        :param str project_id_or_key: Project ID or Project Key

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/versions'.format(project_id_or_key), method='GET')

    def get_webhook(self, project_id_or_key, webhook_id):
        """
        Returns information about webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/projects/{}/webhooks/{}'.format(project_id_or_key, webhook_id), method='GET')

    def update_category(self, project_id_or_key, _id, form_parameters):
        """
        Updates information about Category.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Category ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/categories/{}'.format(
            project_id_or_key, _id), method='PATCH', form_parameters=form_parameters)

    def update_custom_field(self, project_id_or_key, _id, form_parameters):
        """
        Updates Custom Field.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom Field ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/customFields/{}'.format(
            project_id_or_key, _id), method='PATCH', form_parameters=form_parameters)

    def update_issue_type(self, project_id_or_key, _id, form_parameters):
        """
        Updates information about Issue Type.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Issue Type ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/issueTypes/{}'.format(
            project_id_or_key, _id), method='PATCH', form_parameters=form_parameters)

    def update_list_item_for_list_type_custom_field(
            self, project_id_or_key, _id, item_id):
        """
        Updates list item for list type custom field. Calling API fails if specified custom field’s type is not a list.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Custom field ID
        :param int item_id: List item ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/customFields/{}/items/{}'.format(
            project_id_or_key, _id, item_id), method='PATCH')

    def update_project(self, project_id_or_key, form_parameters):
        """
        Updates information about project.

        :param str project_id_or_key: Project ID or Project Key
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}'.format(project_id_or_key),
                             method='PATCH', form_parameters=form_parameters)

    def update_pull_request_comment_information(
            self, project_id_or_key, repo_id_or_name, number, comment_id, form_parameters):
        """
        Updates pull request comment information.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param int comment_id: Comment’s ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}/comments/{}'.format(
            project_id_or_key, repo_id_or_name, number, comment_id), method='PATCH', form_parameters=form_parameters)

    def update_pull_request(self, project_id_or_key,
                            repo_id_or_name, number, form_parameters):
        """
        Updates pull requests.

        :param str project_id_or_key: Project ID or Project Key
        :param str repo_id_or_name: Repository ID or Repository name
        :param int number: Pull request number
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/git/repositories/{}/pullRequests/{}'.format(
            project_id_or_key, repo_id_or_name, number), method='PATCH', form_parameters=form_parameters)

    def update_version_milestone(
            self, project_id_or_key, _id, form_parameters):
        """
        Updates information about Version/Milestone.

        :param str project_id_or_key: Project ID or Project Key
        :param int _id: Version ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/versions/{}'.format(project_id_or_key,
                                                               _id), method='PATCH', form_parameters=form_parameters)

    def update_webhook(self, project_id_or_key, webhook_id, form_parameters):
        """
        Updates information about webhook.

        :param str project_id_or_key: Project ID or Project Key
        :param str webhook_id: Webhook ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/projects/{}/webhooks/{}'.format(project_id_or_key,
                                                               webhook_id), method='PATCH', form_parameters=form_parameters)
