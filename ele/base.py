#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import urllib
import requests
from .exceptions import APIError

BASE_URL = "http://openapi.ele.me/v2"


class EleBase(object):
    """
    The Base class
    """
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    @property
    def base_params(self):
        return {
            "consumer_key": self.consumer_key,
            "timestamp": int(time.time())
        }

    @staticmethod
    def gen_url(uri='/', **kwargs):
        """
        Generate require url
        :param uri: uri with /
        :param kwargs:
        :return:
        """
        sorted_keys = sorted(kwargs.keys())
        if uri[-1] is not '/':
            uri += '/'
        uri += '?'
        for key in sorted_keys:
            if isinstance(kwargs[key], unicode):
                kwargs[key] = urllib.quote_plus(kwargs[key].encode('utf-8'))
            else:
                kwargs[key] = urllib.quote_plus(str(kwargs[key]))
            uri += u'{}={}&'.format(key, kwargs[key])
        return u'%s%s' % (BASE_URL, uri[0:-1])

    def gen_sig_hash(self, url):
        """
        params kwargs: parameters in the request URL, key&value type `unicode`
        return sha1 hex
        """
        to_hash = (url + self.consumer_secret).encode('utf8').encode('hex')

        return hashlib.sha1(to_hash).hexdigest().lower()

    def gen_url_with_sig(self, uri, **kwargs):
        """
        Generate require url with sig
        :return:
        """
        params = self.base_params
        params.update(kwargs)
        url = self.gen_url(uri, **params)
        sig = self.gen_sig_hash(url)
        return u'%s&sig=%s' % (url, sig)

    def _check_error(self, r):
        """
        """
        r.raise_for_status()
        json_data = r.json()
        if "code" in json_data and json_data["message"] != "ok":
            raise APIError(u"{}: {}".format(json_data["code"], json_data["message"]))

    def _request(self, method, uri, **kwargs):
        """
        kwargs中的params 为url参数, data为post 或者put的数据
        """
        sig_params = {}
        ext = {}
        if isinstance(kwargs.get("params"), dict):
            for p_key in kwargs.get("params"):
                sig_params[p_key] = '%s'.encode('utf8') % kwargs.get("params")[p_key]
        if isinstance(kwargs.get("data"), dict):
            for d_key in kwargs.get("data"):
                sig_params[d_key] = '%s'.encode('utf8') % kwargs.get("data")[d_key]
            ext["data"] = kwargs.get("data")

        url = self.gen_url_with_sig(uri, **sig_params)
        r = requests.request(method=method, url=url, **ext)
        self._check_error(r)
        return r.json()

    def _post(self, uri, **kwargs):
        """
        """
        return self._request(
            method="post",
            uri=uri,
            **kwargs
        )

    def _get(self, uri, **kwargs):
        """
        """
        return self._request(
            method="get",
            uri=uri,
            **kwargs
        )

    def _put(self, uri, **kwargs):
        """
        """
        return self._request(
            method="put",
            uri=uri,
            **kwargs
        )
