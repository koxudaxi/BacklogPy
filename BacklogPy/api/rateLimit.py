# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase, SUFFIX_JP


class RateLimit(BacklogBase):
    def __init__(self, space_id, api_key, suffix=SUFFIX_JP):
        super(RateLimit, self).__init__(space_id, api_key, suffix=suffix)

    def get_rate_limit(self):
        """
        Return information about the rate limit currently applied to you.

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request('/rateLimit', method='GET')
