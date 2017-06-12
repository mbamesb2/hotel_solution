#!/usr/bin/env python

from setuptools import find_packages
from distutils.core import setup

setup(
    name="hotel_solution",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.5.3",
        "tornado>=4.1",
    ],
)
