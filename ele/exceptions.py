#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'way'


class NeedParamError(Exception):
    """
    构造参数提供不全异常
    """
    pass


class ParseError(Exception):
    """
    解析数据异常
    """
    pass


class APIError(Exception):
    """
    接口错误
    """
    pass
