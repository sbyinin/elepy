#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from ele.food import Food
from way.test import test_config

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

__author__ = 'way'

clt = Food(**test_config)


def test_get_food_category():
    category = clt.get_food_category(2927739)
    assert category["food_category_id"] == 2927739


def test_get_food_list():
    foods = clt.get_food_list_by_category_id(2927739)
    assert len(foods) > 0


def test_get_food():
    food = clt.get_food(30358057)
    assert food["food_id"] == 30358057


def test_search_food():
    foods = clt.search_food(city_id=1, keyword=u'麦当劳')
    assert len(foods) > 0
