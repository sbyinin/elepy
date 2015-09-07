#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os
from ele.order import Order

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

from way.test import test_config
from ele.cart import Cart

__author__ = 'way'


clt = Order(**test_config)


def test_create_cart():
    food_ids = [30358057]
    # cart = clt.create_cart("18842335250", _create_cart_body(food_ids))
    # assert len(cart["id"]) == 32
    # 073c39bc554911e5a3ddb82a72dc05f8
