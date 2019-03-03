#!/usr/bin/env python
import os
from setuptools import setup

setup(
    name='pstat-simpledb',
    version='0.0.1',
    description='Python SimpleDB API SDK',
    long_description = '',
    author='Michael Malone',
    author_email='mjmalone@gmail.com',
    url='http://github.com/PolicyStat/python-simpledb',
    packages=['simpledb'],
    provides=['simpledb'],
    requires=[
        'httplib2',
        'elementtree',
    ]
)
