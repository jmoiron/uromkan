#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for uromkan."""

from setuptools import setup, find_packages
import sys, os

version = '0.3u'

# some trove classifiers:

# License :: OSI Approved :: MIT License
# Intended Audience :: Developers
# Operating System :: POSIX

setup(
    name='uromkan',
    version=version,
    description="kana <-> romaji conversion and normalization tools",
    long_description=open('README.rst').read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: Japanese",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    keywords='hiragana katakana kana romaji japanese \xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e',
    author='Jason Moiron',
    author_email='jmoiron@jmoiron.net',
    url='http://github.com/jmoiron/uromkan',
    license='GPL',
    py_modules = ['uromkan'],
    #packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    install_requires=[
      # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
