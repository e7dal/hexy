#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imp
import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('readme.txt').read()
history = open('history.txt').read().replace('.. :changelog:', '')
curr_path = os.path.dirname(os.path.realpath(__file__))
deps = os.path.join(curr_path, 'requirements.in')
dev_deps = os.path.join(curr_path, 'dev_requirements.in')

requirements = open(deps).read()
test_requirements = open(dev_deps).read()

CODE_DIRECTORY = 'hexy'
metadata = imp.load_source(
    'metadata', os.path.join(CODE_DIRECTORY, 'metadata.py'))

#orderdict needed for structlog
sys_version_str='.'.join((str(s) for s in sys.version_info[0:3]))


setup(
    name=metadata.package,
    version=metadata.version,
    author=metadata.authors[0],
    author_email=metadata.emails[0],
    maintainer=metadata.authors[0],
    maintainer_email=metadata.emails[0],
    url=metadata.url,
    description=metadata.description,
    long_description=readme + '\n\n' + history,
    packages=[
        'hexy',
        'hexy.util',
        'hexy.commands'
    ],
    package_dir={'hexy':
                 'hexy'},
    py_modules=['hexy'],
    include_package_data=True,
    install_requires=requirements,
    license="GPL-3.0",
    zip_safe=False,
    keywords='hexy, ascii,hexagonal,drawing,toolkit,widgets',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points='''
        [console_scripts]
        hexy = hexy.cli:cli
    '''
)
