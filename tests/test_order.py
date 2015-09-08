#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from ele.order import Order

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')
from config import test_config

__author__ = 'way'


clt = Order(**test_config)


def test_create_order():
    latlng = '31.2397817044,121.5170246832'
    data = {
        "tp_order_id": "12345",
        "phones": "18842335250",
        "address": "1518",
        "cart_id": "073c39bc554911e5a3ddb82a72dc05f8",
        "total": "0.02",
        "longitude": "121.5170246832",
        "latitude": "31.2397817044",
        "ip": "127.0.0.1"
    }
    # order = clt.create_order(**data)
    # print order
    # eleme_order_id = "100002585175710584"


def test_get_order():
    order = clt.get_order(100002585175710584)
    assert order["order_id"] == u'100002585175710584'


def test_get_order_status():
    status = clt.get_order_status(100002585175710584)


def test_get_order_by_tp_id():
    order = clt.get_order_by_tp_id(12345)


def test_get_order_contact_info():
    info = clt.get_order_contact_info(100002585175710584)
    assert info["eleme_order_id"] == u'100002585175710584'


def test_cancel_order():
    cancel = clt.cancel_order(100002585175710584)
    assert cancel is True


def test_update_order_payment_status():
    result = clt.update_order_payment_status(100002585175710584)
    print result
