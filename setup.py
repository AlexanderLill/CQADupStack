#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='CQADupStack',
      version='0.1',
      description='Scripts to query cqadupstack',
      url='https://github.com/D1Doris/CQADupStack',
      author='Doris Hoogeveen',
      author_email='',
      license='Apache',
      packages=['cqadupstack'],
      install=['six', 'scipy', 'nltk'],
      zip_safe=False)
