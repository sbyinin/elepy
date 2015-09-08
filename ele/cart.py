#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ele.base import EleBase

__author__ = 'way'


class Cart(EleBase):
    """
    About cart
    """
    def __init__(self, consumer_key, consumer_secret):
        super(Cart, self).__init__(consumer_key, consumer_secret)

    def create_cart(self, phone, food):
        uri = '/cart/'
        post_data = {
            "phone": phone,
            "food": food
        }
        re_data = self._post(uri, data=post_data)
        return re_data.get("data")

    def update_cart(self, cart_id, phone, food):
        uri = '/cart/%s/' % cart_id
        put_data = {
            "phone": phone,
            "food": food
        }
        re_data = self._put(uri, data=put_data)
        return re_data.get("data")

