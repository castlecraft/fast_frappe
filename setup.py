from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in fast_frappe/__init__.py
from fast_frappe import __version__ as version

setup(
	name='fast_frappe',
	version=version,
	description='FastAPI using Frappe Framework',
	author='Revant Nandgaonkar',
	author_email='support@castlecraft.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
