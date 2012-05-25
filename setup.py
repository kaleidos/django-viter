#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import viter

setup(
    name='django-viter',
    version=":versiontools:viter:",
    description='Invite users to your Django apps',
    long_description=open('README.rst').read(),
    author='Jesús Espino',
    author_email='jespinog@gmail.com',
    packages=find_packages(),
    package_data={
        'viter': [
            'templates/viter/email/*',
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    include_package_data=True,
    zip_safe=False,
)
