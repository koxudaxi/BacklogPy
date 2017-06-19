# coding: utf-8

"""
    This file was created by Backlog APIGenerator
"""


from __future__ import unicode_literals, absolute_import

from BacklogPy.base import BacklogBase


class Stars(BacklogBase):
    def __init__(self, space_id, api_key):
        super(Stars, self).__init__(space_id, api_key)

    def add_star(self, form_parameters):
        """
        Adds star.

        :param dict form_parameters: form_parameters

        :return:  requests Response object
        :rtype requests.Response
        """
        return self._request('/stars', method='POST',
                             form_parameters=form_parameters)
