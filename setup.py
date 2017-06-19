# -*- coding: utf-8 -*-

import sys

from setuptools import setup

packages = ['BacklogPy', 'BacklogPy.api']

__version__ = '0.5.2'

requires = [
    'requests'
]

test_requirements = ['mock', 'nose']
if sys.version_info < (2, 7, 0):
    test_requirements.append('unittest2')

with open('LICENSE', 'r') as f:
    _license = f.read()

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='BacklogPy',
    version=__version__,
    description='Backlog API v2 Client Library',
    long_description=readme,
    author='Koudai Aono',
    author_email='koxudaxi@gmail.com',
    url='https://github.com/koxudaxi/BacklogPy',
    packages=packages,
    data_files=[('', ['LICENSE', 'README.rst'])],
    package_dir={'BacklogPy': 'BacklogPy'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    setup_requires=['nose>=1.0'],
    tests_require=test_requirements,
)
