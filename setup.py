#!/usr/bin/env python
import os
import urllib

from setuptools import setup, find_packages, Command

import criticalpath

setup(
    name = "criticalpath",
    version = criticalpath.__version__,
    py_modules=['criticalpath'],
    author = "Chris Spencer",
    author_email = "chrisspen@gmail.com",
    description = "Calculates the critical path in a task network.",
    license = "LGPL",
    url = "https://github.com/chrisspen/criticalpath",
    #https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe = False,
)
