#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

from way.test import test_config
from ele.city import City

__author__ = 'way'


clt = City(**test_config)


class TestCity(object):

    def test_get_cities(self):
        cities = clt.get_city_list()
        assert len(cities) > 0
