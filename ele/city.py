#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ele.base import EleBase

__author__ = 'way'


class City(EleBase):
    """
    About city
    """
    def __init__(self, consumer_key, consumer_secret):
        super(City, self).__init__(consumer_key, consumer_secret)

    def get_city_list(self):
        uri = '/cities'
        data = self._get(uri).get("data", {})
        return data.get("cities")
