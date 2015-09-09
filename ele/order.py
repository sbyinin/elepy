#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import EleBase


class Order(EleBase):
    """
    About Order
    """
    def __init__(self, consumer_key, consumer_secret):
        super(Order, self).__init__(consumer_key, consumer_secret)

    def create_order(self, tp_order_id, phones, address, cart_id, total, longitude,
                     latitude, ip, deliver_time=None, description=None, invoice=None,
                     is_online_paid=None, validation=None):
        """
        :return: order
        """
        uri = '/order/'
        post_data = {
            "tp_order_id": tp_order_id,
            "phones": phones,
            "address": address,
            "cart_id": cart_id,
            "total": total,
            "longitude": longitude,
            "latitude": latitude,
            "ip": ip
        }

        if deliver_time:
            post_data["deliver_time"] = deliver_time
        if description:
            post_data["description"] = description
        if invoice:
            post_data["invoice"] = invoice
        if is_online_paid:
            post_data["is_online_paid"] = is_online_paid
        if validation:
            post_data["validation"] = validation

        re_data = self._post(uri, data=post_data).get("data")
        return re_data

    def get_order(self, eleme_order_id):
        uri = '/order/%s/' % eleme_order_id
        re_data = self._get(uri).get("data")
        return re_data

    def get_order_status(self, eleme_order_id):
        uri = '/order/%s/status/' % eleme_order_id
        re_data = self._get(uri).get("data")
        return re_data

    def get_order_by_tp_id(self, tp_order_ids):
        uri = '/orders/tp_order_id/'
        params = {
            "tp_order_ids": tp_order_ids
        }
        re_data = self._get(uri, params=params).get("data")
        return re_data

    def get_order_contact_info(self, eleme_order_id):
        uri = '/order/%s/contact_info/' % eleme_order_id
        re_data = self._get(uri).get("data")
        return re_data

    def cancel_order(self, eleme_order_id, status=-1, type_=1, reason=""):
        """
        :param eleme_order_id:
        :param reason:
        :return:
        """
        uri = '/order/%s/status/' % eleme_order_id
        assert status == -1
        assert type_ in [1, 2, 3]
        if type_ == 2:
            assert reason
        post_data = {
            "status": status,
            "type": type_,
        }
        if reason:
            post_data["reason"] = reason
        re_data = self._put(uri, data=post_data)
        return re_data["code"] == 200

    def update_order_payment_status(self, eleme_order_id):
        """
        data.status 只能是1 表示支付成功
        :param eleme_order_id:
        :return:
        """
        uri = '/order/%s/payment_status/' % eleme_order_id
        post_data = {
            "status": 1
        }
        re_data = self._put(uri, data=post_data)
        return re_data["code"] == 200
