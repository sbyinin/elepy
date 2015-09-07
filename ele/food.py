#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ele.base import EleBase

__author__ = 'way'


class Food(EleBase):
    """
    about food
    """
    def __init__(self, consumer_key, consumer_secret):
        super(Food, self).__init__(consumer_key, consumer_secret)

    def get_food_category(self, food_category_id):
        uri = '/food_category/%s/' % food_category_id
        data = self._get(uri).get("data", {})
        return data.get("food_category")

    def get_food_list_by_category_id(self, food_category_id):
        uri = '/food_category/%s/foods' % food_category_id
        data = self._get(uri).get("data", {})
        return data.get("foods")

    def get_food(self, food_id):
        uri = '/food/%s/' % food_id
        data = self._get(uri).get("data", {})
        return data.get("food")

    def search_food(self, **kwargs):
        uri = '/foods'
        data = self._get(uri, params=kwargs).get("data", {})
        return data.get("foods")
