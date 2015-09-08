#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')
from ele.restaurant import Restaurant
from config import test_config

__author__ = 'way'

restaurant_id = 28705300
clt = Restaurant(**test_config)


def test_search_restaurants_count():
    count = clt.search_restaurants_count("121.5170246832,31.2397817044", 1, u'小吃')
    assert count > 0


def test_get_restaurant():
    restaurant = clt.get_restaurant(restaurant_id)
    assert restaurant["restaurant_id"] == restaurant_id


def test_get_restaurant_food_list():
    cates = clt.get_restaurant_food_category_list(restaurant_id)
    assert len(cates) > 0


def test_get_restaurant_menu():
    menu = clt.get_restaurant_menu(restaurant_id)
    assert len(menu) > 0


def test_get_restaurant_deliver_amount():
    amount = clt.get_restaurant_deliver_amount(restaurant_id, "121.5170246832,31.2397817044")
    print amount
    # TODO:: 系统异常


def test_get_restaurant_flavor_list():
    flavors = clt.get_restaurant_flavor_list()
    assert len(flavors) > 0


