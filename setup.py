#!/usr/bin/env python

import setuptools
from setuptools import setup

setup(name='access-spotify',
      version='1.9',
      author='pancham_banerjee',
      packages=setuptools.find_packages(),
      scripts=['./bin/access_script.py'],
      )

