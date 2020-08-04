#!/usr/bin/env python

import setuptools
from setuptools import setup

with open("requirements.txt", "r") as f:
    requirements = [line.rstrip("\n") for line in f if line != "\n"]

setup(name='access-spotify',
      version="1.0",
      author="pancham_banerjee",
      author_email="panchajanya.banerjee@gmail.com",
      packages=setuptools.find_packages(),
      scripts=["./bin/access_script.py"],
      install_requires=requirements,
      license="MIT",
      description="A package to get all album and track info for an artist by querying the Spotify API"
      )

