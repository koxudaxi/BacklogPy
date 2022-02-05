# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase, SUFFIX_JP


class Activities(BacklogBase):
    def __init__(self, space_id, api_key, suffix=SUFFIX_JP):
        super(Activities, self).__init__(space_id, api_key, suffix=suffix)

    def get_space_activity(self, activity_id):
        """
        Returns an activity

        :param int activity_id: activity ID

        :return:  requests Response object
        :rtype: requests.Response
        """

        return self._request(
            '/activities/{}'.format(activity_id),
            method='GET')
