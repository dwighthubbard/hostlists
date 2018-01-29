#!/usr/bin/env python
"""
Setup configuration for hostlists
"""

# Copyright (c) 2010-2015 Yahoo! Inc. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. See accompanying LICENSE file.

from setuptools import setup
import sys


METADATA_FILENAME = 'hostlists/metadata.json'


# Python2 and Python3 have different requirements
requirements = ['requests']
if sys.version > '3.0.0':
    requirements.append('dnspython3')
else:
    requirements.append('dnspython')


setup_args = {
    'name': 'hostlists',
    'version': '0.8.0',
    'author': 'Dwight Hubbard',
    'author_email': 'dhubbard@yahoo-inc.com',
    'url': 'https://github.com/yahoo/hostlists',
    'license': 'LICENSE.txt',
    'packages': ['hostlists', 'hostlists.plugins', 'hostlists_plugins_default'],
    'long_description': open('README.rst').read(),
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities'
    ],
    'description': 'A python library to obtain lists of hosts from various '
                   'systems',
    'requires': requirements,
    'install_requires': requirements,
}


if __name__ == '__main__':
    setup(**setup_args)
