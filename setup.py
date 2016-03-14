#!/usr/bin/env python
# # coding: utf-8
from setuptools import find_packages, setup

with open('README.rst') as readme:
    long_description = readme.read()

name = "sdate"
version = "0.1.0"
author = "qiueer"

setup(
    name=name,
    description='simple datetime',
    version=version,
    long_description=long_description,
    author=author,
    author_email='qiujqin@163.com',
    url='https://github.com/qiueer/%s' % (name),
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: GNU Library or Lesser '
         'General Public License (LGPL)'),
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
