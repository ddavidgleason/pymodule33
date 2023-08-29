from setuptools import setup, find_packages

setup(
    name='myexecutable',
    version='0.2',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    python_requires='>=3',
    author='David',
    author_email='ddickson@gleason.com',
    description='A simple Python package',
)
