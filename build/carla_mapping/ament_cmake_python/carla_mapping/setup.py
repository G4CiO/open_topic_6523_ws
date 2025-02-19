from setuptools import find_packages
from setuptools import setup

setup(
    name='carla_mapping',
    version='0.0.0',
    packages=find_packages(
        include=('carla_mapping', 'carla_mapping.*')),
)
