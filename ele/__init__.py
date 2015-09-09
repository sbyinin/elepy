#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .cart import Cart
from .city import City
from .food import Food
from .order import Order
from .rating import Rating
from .restaurant import Restaurant


class Client(object):
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    @property
    def cart(self):
        return Cart(self.consumer_key, self.consumer_secret)

    @property
    def city(self):
        return City(self.consumer_key, self.consumer_secret)

    @property
    def food(self):
        return Food(self.consumer_key, self.consumer_secret)

    @property
    def order(self):
        return Order(self.consumer_key, self.consumer_secret)

    @property
    def rating(self):
        return Rating(self.consumer_key, self.consumer_secret)

    @property
    def restaurant(self):
        return Restaurant(self.consumer_key, self.consumer_secret)
