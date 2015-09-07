#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ele.base import EleBase

__author__ = 'way'


class Rating(EleBase):
    """
    About rating
    """
    def __init__(self, consumer_key, consumer_secret):
        super(Rating, self).__init__(consumer_key, consumer_secret)

    def get_order_items_to_rate(self, eleme_order_id):
        uri = '/rating/items/'
        params = {
            "order_id": eleme_order_id
        }
        data = self._get(uri, params=params).get("data", {})
        return data.get("items", [])

    def create_order_rating(self, eleme_order_id, service_rating, service_rating_text, comment_time, deliver_time=None):
        """
        订单评价
        :param eleme_order_id:  eleme 订单号
        :param service_rating:  服务等级(1-5)
        :param service_rating_text: 服务评价
        :param comment_time:    评论时间
        :param deliver_time:    送达时间
        :return:    True or False
        """
        uri = '/rating/order/%s/' % eleme_order_id
        data = {
            "service_rating": service_rating,
            "service_rating_text": service_rating_text,
            "comment_time": comment_time,
        }
        if deliver_time:
            data['deliver_time'] = deliver_time
        re = self._post(uri, data=data)
        return re["code"] == 200

    def create_food_rating(self, item_id, rating, rating_text):
        """
        菜品评价
        :param item_id:
        :param rating:
        :param rating_text:
        :return:
        """
        uri = '/rating/item/%s/' % item_id
        data = {
            "rating": rating,
            "rating_text": rating_text
        }
        re = self._post(uri, data=data)
        return re["code"] == 200
