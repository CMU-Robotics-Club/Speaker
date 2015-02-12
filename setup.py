#!/usr/bin/env python

import os
from setuptools import setup

from speaker import __client__, __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = __client__,
    version = __version__,
    author = "Brent Strysko",
    author_email = "bstrysko@andrew.cmu.edu",
    description = ("CMU Robotics Club Speaker"),
    license = "MIT",
    keywords = "roboclub robotics club api cmu speaker",
    packages=['speaker/',],
    scripts = ["bin/speaker"],
    long_description=read('README.md'),
    dependency_links = [
        'https://github.com/CMU-Robotics-Club/pyrc/tarball/master#egg=pyrc-1.0',
    ],
    install_requires = [
        'daemonize',
        'psutil',
        'pafy',
        'pyrc',
    ],
)