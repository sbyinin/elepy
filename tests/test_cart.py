#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

from config import test_config
from ele.cart import Cart

__author__ = 'way'


clt = Cart(**test_config)


def _create_cart_body(food_ids):
    group_1 = []
    for food_id in food_ids:
        food_to_add = {
            'id': food_id,
            'quantity': 2,
            'garnish': []
        }
        group_1.append(food_to_add)

    return json.dumps({
        'group': [
            group_1,
            [],
        ],
    })


def test_create_cart():
    food_ids = [30358057]
    # cart = clt.create_cart("18842335250", _create_cart_body(food_ids))
    # assert len(cart["id"]) == 32
    # 073c39bc554911e5a3ddb82a72dc05f8
