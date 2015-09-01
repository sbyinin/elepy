# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ele-sdk',
    version='0.0.1',
    keywords=('eleme', 'ele', 'eleme open api'),
    description=u'饿了么开放接口SDK',
    long_description=open("README.md").read(),
    license='MIT License',

    url='https://github.com/prowayne/elepy',
    author='prowayne',
    author_email='hongwei.liu@ele.me',

    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=map(lambda x: x.replace('==', '>='), open("requirements.txt").readlines()),
)