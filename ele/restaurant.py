#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ele.base import EleBase

__author__ = 'way'


class Restaurant(EleBase):
    """
    About restaurant
    """
    def __init__(self, consumer_key, consumer_secret):
        super(Restaurant, self).__init__(consumer_key, consumer_secret)

    def search_restaurants(self, **kwargs):
        """
        """
        uri = '/restaurants'
        data = self._get(uri, params=kwargs).get("data", {})
        return data.get("restaurants", [])

    def get_restaurant(self, restaurant_id):
        """
        Get restaurant by restaurant_id
        :param restaurant_id:
        :return:
        """
        uri = '/restaurant/%s/' % restaurant_id
        data = self._get(uri).get("data", {})
        return data.get("restaurant")

    def get_restaurant_food_category_list(self, restaurant_id):
        # TODO :: permission error
        uri = '/restaurant/%s/food_categories/' % restaurant_id
        data = self._get(uri).get("data", {})
        return data.get("food_categories", [])
