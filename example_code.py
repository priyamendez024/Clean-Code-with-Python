# Chapter 23: Packaging and Distributing Python Code

# setup.py example
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    author='Your Name',
    description='Example Python package'
)