# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Wikis(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Wikis, self).__init__(space_id, api_key)

    def add_wiki_page(self, form_parameters):
        """
        Adds new Wiki page.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis', method='POST',
                             form_parameters=form_parameters)

    def attach_file_to_wiki(self, wiki_id, form_parameters):
        """
        Attaches file to Wiki

        :param int wiki_id: Wiki page’s ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis/{}/attachments'.format(wiki_id),
                             method='POST', form_parameters=form_parameters)

    def count_wiki_page(self, query_parameters):
        """
        Returns number of Wiki pages.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis/count', method='GET',
                             query_parameters=query_parameters)

    def delete_wiki_page(self, wiki_id):
        """
        Deletes Wiki page.

        :param int wiki_id: Wiki page ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis/{}'.format(wiki_id), method='DELETE')

    def get_list_of_shared_files_on_wiki(self, wiki_id):
        """
        Returns the list of Shared Files on Wiki.

        :param int wiki_id: Wiki page’s ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/wikis/{}/sharedFiles'.format(wiki_id), method='GET')

    def get_list_of_wiki_attachments(self, wiki_id):
        """
        Gets list of files attached to Wiki.

        :param int wiki_id: Wiki page’s ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/wikis/{}/attachments'.format(wiki_id), method='GET')

    def get_wiki_page_attachment(self, wiki_id, attachment_id):
        """
        Downloads Wiki page’s attachment file.

        :param int wiki_id: Wiki Page ID
        :param int attachment_id: Attachment file ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/wikis/{}/attachments/{}'.format(wiki_id, attachment_id), method='GET')

    def get_wiki_page_history(self, wiki_id, query_parameters):
        """
        Returns history of Wiki page.

        :param int wiki_id: Wiki Page ID
        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis/{}/history'.format(wiki_id),
                             method='GET', query_parameters=query_parameters)

    def get_wiki_page_list(self, query_parameters):
        """
        Returns list of Wiki pages.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis', method='GET',
                             query_parameters=query_parameters)

    def get_wiki_page_star(self, wiki_id):
        """
        Returns list of stars received on the Wiki page.

        :param int wiki_id: Wiki Page ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis/{}/stars'.format(wiki_id), method='GET')

    def get_wiki_page_tag_list(self, query_parameters):
        """
        Returns list of tags that are used in the project.

        :param dict query_parameters: query_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis/tags', method='GET',
                             query_parameters=query_parameters)

    def get_wiki_page(self, wiki_id):
        """
        Returns information about Wiki page.

        :param int wiki_id: Wiki page ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis/{}'.format(wiki_id), method='GET')

    def link_shared_files_to_wiki(self, wiki_id):
        """
        Links Shared Files to Wiki.

        :param int wiki_id: Wiki page’s ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/wikis/{}/sharedFiles'.format(wiki_id), method='POST')

    def remove_link_to_shared_file_from_wiki(self, wiki_id, _id):
        """
        Removes link to shared file from Wiki.

        :param int wiki_id: Wiki page’s ID
        :param int _id: Shared file ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/wikis/{}/sharedFiles/{}'.format(wiki_id, _id), method='DELETE')

    def remove_wiki_attachment(self, wiki_id, attachment_id):
        """
        Removes files attached to Wiki.

        :param int wiki_id: Wiki page’s ID
        :param int attachment_id: Attachment’s ID

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request(
            '/wikis/{}/attachments/{}'.format(wiki_id, attachment_id), method='DELETE')

    def update_wiki_page(self, wiki_id, form_parameters):
        """
        Updates information about Wiki page.

        :param int wiki_id: Wiki page ID
        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/wikis/{}'.format(wiki_id),
                             method='PATCH', form_parameters=form_parameters)
