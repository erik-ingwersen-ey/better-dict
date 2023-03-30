#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from setuptools import setup
from pathlib import Path


requirements_path = Path('requirements.txt').resolve()

if requirements_path.is_file():
    with open(
        requirements_path,
        errors='ignore',
        encoding='utf-8',
        buffering=1,
        mode='r',
    ) as fp:
        requirements = fp.read().splitlines()
else:
    print('No requirements.txt found. Skipping.')
    requirements = []  # Empty requirements list to avoid errors.

setup(
    name='better-dict',
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': 'src/better_dict/_version.py',
        'fallback_version': '0.0.1',
    },
    description="Python dictionary revamped.",
    license="MIT",
    author="Erik Ingwersen",
    author_email='erik.ingwersen@br.ey.com',
    url='https://github.com/ingwersen-erik/better-dict',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    package_dir={'': 'src'},
    packages=['better_dict'],
    # entry_points={
    #     'console_scripts': [
    #         'better_dict=better_dict.cli:main'
    #     ]
    # },
    install_requires=requirements,
    keywords='better-dict',
    setup_requires=['setuptools_scm'],
)
