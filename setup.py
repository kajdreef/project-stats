#/usr/bin/env python3
# -*- coding: utf-8 -*-
from distutils.core import setup

from project_stats import __version__

setup(
    name='project-stats',
    version=__version__,
    packages=['project_stats',],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'project-stats=project_stats.cli:main'
        ]
    }
)
