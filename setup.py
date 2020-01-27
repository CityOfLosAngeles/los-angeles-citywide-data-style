"""The setup script."""
from setuptools import setup, find_packages
from os.path import exists

from los_angeles_citywide_data_style._version import __version__ as version

readme = open("README.md").read() if exists("README.md") else ""


setup(
    name="los_angeles_citywide_data_style",
    description="Style package for City of Los Angeles data science projects",
    long_description=readme,
    long_description_content_type="text/markdown",
    maintainer="Ian Rose",
    maintainer_email="ian.rose@lacity.org",
    url="https://github.com/CityOfLosAngeles/los-angeles-citywide-data-style",
    packages=find_packages(),
    package_data={"los_angeles_citywide_data_style": ["*.mplstyle"]},
    package_dir={"los-angeles-citywide-data-style": "los-angeles-citywide-data-style"},
    include_package_data=True,
    install_requires=["matplotlib>=1.5"],
    license="Apache-2.0 license",
    zip_safe=False,
    keywords="matplotlib",
    version=version,
)
