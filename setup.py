#!/usr/bin/env python

import setuptools
from setuptools import setup
from os import path

# Read the package requirements
with open("requirements.txt", "r") as f:
    requirements = [line.rstrip("\n") for line in f if line != "\n"]

# Read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='access-spotify',
      version="1.1",
      author="pancham_banerjee",
      author_email="panchajanya.banerjee@gmail.com",
      packages=setuptools.find_packages(),
      scripts=["./bin/access_script.py"],
      install_requires=requirements,
      license="MIT",
      description="A package to get all album and track info for an artist by querying the Spotify API",
      long_description=long_description,
      long_description_content_type='text/markdown'
      )

