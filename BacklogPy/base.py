# coding: utf-8


from __future__ import unicode_literals, print_function, absolute_import

from logging import getLogger, INFO

import requests

logger = getLogger(__name__)
logger.setLevel(INFO)

X_WWW_FROM_URLENCODED_HEADERS = {
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
}

BACKLOG_URL = 'backlog.jp'

API_ROOT = 'api/v2'


class BacklogBase(object):
    def __init__(self, space_id, api_key):
        """"
        :param space_id:  
        :param api_key:
        
        :type space_id: str
        :type api_key: str
        """

        self._api_key = api_key
        self._api_url = 'https://{space_id}.{backlog_server}/{api_root}' \
            .format(space_id=space_id, backlog_server=BACKLOG_URL,
                    api_root=API_ROOT)

    def _request(self, path, method='GET',
                 query_parameters=None, form_parameters=None,
                 headers=None):
        """
        
        :param unicode path: 
        :param unicode method: 
        :param dict query_parameters: 
        :param dict form_parameters: 
        :param dict headers: 
        :return: requests Response Object
        :rtype requests.Response
        """

        url = self._api_url + path

        if form_parameters:
            headers = X_WWW_FROM_URLENCODED_HEADERS
        else:
            form_parameters = {}

        if query_parameters is None:
            query_parameters = {}

        query_parameters['apiKey'] = self._api_key

        if headers is None:
            headers = {}

        logger.debug(
            'request api method:{method} url:{url} \
            query_parameters:{query_parameters} \
            form_parameters:{form_parameters} headers:{headers}'
                .format(method=method, url=url,
                        query_parameters=query_parameters,
                        form_parameters=form_parameters,
                        headers=headers))

        return requests.request(method, url,
                                params=query_parameters,
                                data=form_parameters,
                                headers=headers)
