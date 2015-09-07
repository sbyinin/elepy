#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from ele.restaurant import Restaurant
from way.test import test_config

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

__author__ = 'way'

restaurant_id = 28705300
clt = Restaurant(**test_config)


def test_get_restaurant():
    restautant = clt.get_restaurant(restaurant_id)
    assert restautant["restaurant_id"] == restaurant_id


def test_get_restaurant_food_list():
    cates = clt.get_restaurant_food_category_list(restaurant_id)
    assert len(cates) > 0

