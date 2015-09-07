#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ele.base import EleBase

__author__ = 'way'


class Image(EleBase):
    """
    About image
    """
    def __init__(self, consumer_key, consumer_secret):
        super(Image, self).__init__(consumer_key, consumer_secret)

    def upload_restaurant_image(self):
        pass