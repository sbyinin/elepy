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
        return data.get("restaurants")

    def search_restaurants_count(self, geo, is_inside=1, keyword=''):
        """
        Get restaurant count
        :param  geo: String "lng,lat"
        :return: Int
        """
        uri = '/restaurants/count/'
        params = {
            "geo": geo,
            "is_inside": is_inside,
        }
        if keyword:
            params["keyword"] = keyword
        data = self._get(uri, params=params).get("data", {})
        return data.get("count")

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
        uri = '/restaurant/%s/food_categories/' % restaurant_id
        data = self._get(uri).get("data", {})
        return data.get("food_categories")

    def get_restaurant_menu(self, restaurant_id, tp_id=0):
        """
        菜单
        :param restaurant_id:
        :param tp_id: 暂不使用
        :return:
        """
        uri = '/restaurant/%s/menu/' % restaurant_id
        params = {
            # "tp_id": tp_id
        }
        data = self._get(uri, params=params).get("data", {})
        return data.get("restaurant_menu")

    def get_restaurant_deliver_amount(self, restaurant_id, geo):
        """
        餐厅起送价
        :param restaurant_id:
        :param geo:
        :return:
        """
        uri = '/restaurant/%s/deliver_amount/' % restaurant_id
        params = {
            "geo": geo
        }
        data = self._get(uri, params=params).get("data", {})
        return data.get("deliver_amount")

    def get_restaurant_flavor_list(self):
        """
        可选口味列表
        :return: List
        """
        uri = '/restaurant/flavors/'
        data = self._get(uri).get("data", {})
        return data.get("flavors")


