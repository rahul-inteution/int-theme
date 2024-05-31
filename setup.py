from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in business_theme_v14/__init__.py
from int_theme import __version__ as version

setup(
	name="int_theme",
	version=version,
	description="int Theme for ERPNext / Frappe",
	author="Rahul",
	author_email="rahul@inteution.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
