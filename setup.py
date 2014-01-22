# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='easytmdb',
    version='0.1.1',
    author='Tómas Þór Jónsson',
    author_email='benregn@gmail.com',
    description='A Python wrapper for The Movie Database API v3',
    keywords=['movie', 'the movie database', 'movie database', 'tmdb',
              'wrapper', 'api'],
    url='https://github.com/benregn/easytmdb',
    packages=['easytmdb'],
    long_description=read('README.rst'),
    install_requires=['requests>=0.11.1'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)
