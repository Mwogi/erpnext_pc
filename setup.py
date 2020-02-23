# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in performance_contracting/__init__.py
from performance_contracting import __version__ as version

setup(
	name='performance_contracting',
	version=version,
	description='Tracking performance contracts for the organization',
	author='Thomas Mwogi',
	author_email='erp@mtrh.go.ke',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
