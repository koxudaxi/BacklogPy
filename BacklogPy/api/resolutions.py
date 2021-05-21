# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase, SUFFIX_JP


class Resolutions(BacklogBase):
    def __init__(self, space_id, api_key, suffix=SUFFIX_JP):
        super(Resolutions, self).__init__(space_id, api_key, suffix=suffix)

    def get_resolution_list(self):
        """
        Returns list of resolutions.

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/resolutions', method='GET')
