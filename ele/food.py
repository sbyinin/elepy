#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import EleBase


class Food(EleBase):
    """
    About food
    """
    def __init__(self, consumer_key, consumer_secret):
        super(Food, self).__init__(consumer_key, consumer_secret)

    def get_food_category(self, food_category_id):
        uri = '/food_category/%s/' % food_category_id
        re_data = self._get(uri).get("data", {})
        return re_data.get("food_category")

    def get_food_list_by_category_id(self, food_category_id):
        uri = '/food_category/%s/foods/' % food_category_id
        re_data = self._get(uri).get("data", {})
        return re_data.get("foods")

    def get_food(self, food_id):
        uri = '/food/%s/' % food_id
        re_data = self._get(uri).get("data", {})
        return re_data.get("food")

    def search_food(self, **kwargs):
        uri = '/foods/'
        re_data = self._get(uri, params=kwargs).get("data", {})
        return re_data.get("foods")
