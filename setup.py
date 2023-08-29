from setuptools import setup, find_packages

setup(
    name='myexecutable',
    version='0.2',
    packages=find_packages(where='src'),
    install_requires=[],
    author='David',
    author_email='ddickson@gleason.com',
    description='A simple Python package',
)
