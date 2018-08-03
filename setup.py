#!/usr/bin/env python
# encoding: utf-8

import setuptools

from app import version

__author__ = 'ingbyr'

setuptools.setup(
    name='BUPTNetLogin',
    version=version,
    author='ingbyr',
    author_email='ingbyr@outlook.com',
    url='https://www.ingbyr.com',
    description='Command line tool to login the BUPT net',
    packages=['app'],
    install_requires=[
        'requests',
        'lxml'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bnl = app.bupt_net_login:enter',
        ]
    },
)
