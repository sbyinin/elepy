#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')
from ele.rating import Rating
from config import test_config

__author__ = 'way'

clt = Rating(**test_config)


def test_get_order_items_to_rate():
    items = clt.get_order_items_to_rate(100002585175710584)
    print items


def test_create_order_rating():
    result = clt.create_order_rating(100002585175710584, 5, u'一般', '2015-09-08 11:45:11', '2015-09-08 11:41:11')
    print result


def test_create_food_rating():
    result = clt.create_food_rating(1337234069, 5, u'nice')
    print result

