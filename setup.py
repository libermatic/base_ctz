# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# get version from __version__ variable in base_ctz/__init__.py
from base_ctz import __version__ as version

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")


setup(
    name="base_ctz",
    version=version,
    description="Base Customization",
    author="Libermatic",
    author_email="info@libermatic.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
