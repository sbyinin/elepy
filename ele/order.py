#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ele.base import EleBase

__author__ = 'way'


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
        :param  tp_order_id	string	是	第三方订单id（需保证唯一）
        :param  phones	    string	是	电话号码，主要号码必须是手机号
        :param  address	    string	是	送餐地址（用户地址）
        :param  cart_id	    string	是	购物车ID
        :param  total	    string	是	订单总金额，从饿了么返回的购物车里获得，类型由float转为string
        :param  longitude	float	是	订单来源地址经度
        :param  latitude	float	是	订单来源地址纬度
        :param  ip	        string	是	订单来源ip地址
        :param  deliver_time	datetime	否	预定送达时间，留空表示立刻送出，参考 预订单说明
        :param  description	string	否	订单备注信息
        :param  invoice	    string	否	发票抬头（个人发票请填写个人），不传表示不要发票
        :param  is_online_paid	int	否	是否在线支付订单（在线支付为1，非在线支付为0）
        :param  validation	string	否	仅在线支付订单需要传递此参数，参考 在线支付验证
        :return:
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
        data = self._get(uri).get("data")
        return data

    def get_order_status(self, eleme_order_id):
        uri = '/order/%s/status/' % eleme_order_id
        data = self._get(uri).get("data")
        return data

    def get_order_by_tp_id(self, tp_order_ids):
        uri = '/orders/tp_order_id/'
        params = {
            "tp_order_ids": tp_order_ids
        }
        data = self._get(uri, params=params).get("data")
        return data

    def get_order_contact_info(self, eleme_order_id):
        uri = '/order/%s/contact_info/' % eleme_order_id
        data = self._get(uri).get("data")
        return data

    def cancel_order(self, eleme_order_id, reason=""):
        """
        :param eleme_order_id:
        :param reason:
        :return:
        """
        uri = '/order/%s/status/' % eleme_order_id
        data = {
            "status": -1,
            "type": 1,
        }
        if reason:
            data["reason"] = reason
        re_data = self._put(uri, data=data)
        return re_data["code"] == 200

    def update_order_payment_status(self, eleme_order_id):
        """
        data.status 只能是1 表示支付成功
        :param eleme_order_id:
        :return:
        """
        uri = '/order/%s/payment_status/' % eleme_order_id
        data = {
            "status": 1
        }
        re_data = self._put(uri, data=data)
        return re_data["code"] == 200





