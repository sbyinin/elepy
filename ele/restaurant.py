#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import EleBase


class Restaurant(EleBase):
    """
    About restaurant
    """
    def __init__(self, consumer_key, consumer_secret):
        super(Restaurant, self).__init__(consumer_key, consumer_secret)

    def search_restaurants(self, geo, restaurant_ids=None, keyword=None,
                           city_id=None, order_by=None, busy_level=None,
                           flavor=None, invoice=None, payment=None, offset=None,
                           limit=None):
        """
        """
        params = {
            "geo": geo,
            "restaurant_ids": restaurant_ids,
            "keyword": keyword,
            "city_id": city_id,
            "order_by": order_by,
            "busy_level": busy_level,
            "flavor": flavor,
            "invoice": invoice,
            "payment": payment,
            "offset": offset,
            "limit": limit
        }

        uri = '/restaurants'
        re_data = self._get(uri, params=params).get("data", {})
        return re_data.get("restaurants")

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
        re_data = self._get(uri, params=params).get("data", {})
        return re_data.get("count")

    def get_restaurant(self, restaurant_id):
        """
        Get restaurant by restaurant_id
        :param restaurant_id:
        :return:
        """
        uri = '/restaurant/%s/' % restaurant_id
        re_data = self._get(uri).get("data", {})
        return re_data.get("restaurant")

    def get_restaurant_food_category_list(self, restaurant_id):
        """
        """
        uri = '/restaurant/%s/food_categories/' % restaurant_id
        re_data = self._get(uri).get("data", {})
        return re_data.get("food_categories")

    def get_restaurant_menu(self, restaurant_id):
        """
        菜单
        :param restaurant_id:
        :return:
        """
        uri = '/restaurant/%s/menu/' % restaurant_id
        re_data = self._get(uri).get("data", {})
        return re_data.get("restaurant_menu")

    def get_restaurant_flavor_list(self):
        """
        可选口味列表
        :return: List
        """
        uri = '/restaurant/flavors/'
        re_data = self._get(uri).get("data", {})
        return re_data.get("flavors")
