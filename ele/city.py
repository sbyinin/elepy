#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import EleBase


class City(EleBase):
    """
    About city
    """
    def __init__(self, consumer_key, consumer_secret):
        super(City, self).__init__(consumer_key, consumer_secret)

    def get_city_list(self):
        uri = '/cities/'
        re_data = self._get(uri).get("data", {})
        return re_data.get("cities")
