#!/usr/bin/env python
"""
Setup configuration for hostlists
"""
__license__ = """
 Copyright (c) 2010-2014 Yahoo! Inc. All rights reserved.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License. See accompanying LICENSE file.
"""
from distutils.core import setup
import json
import os
import sys


METADATA_FILENAME = 'hostlists/metadata.json'


# Python2 and Python3 have different requirements
requirements = []
if sys.version > '3.0.0':
    requirements.append('dnspython3')
else:
    requirements.append('dnspython')


setup_args = {
    'name': 'hostlists',
    'version': '0.7.10',
    'author': 'Dwight Hubbard',
    'author_email': 'dhubbard@yahoo-inc.com',
    'url': 'https://github.com/yahoo/hostlists',
    'license': 'LICENSE.txt',
    'packages': ['hostlists', 'hostlists.plugins'],
    'scripts': ['hostlists/hostlists'],
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities'
    ],
    'description': 'A python library to obtain lists of hosts from various '
                   'systems',
    'requires': requirements,
    'install_requires': requirements,
}


class Git(object):
    version_list = ['0', '7', '0']

    def __init__(self, version=None):
        if version:
            self.version_list = version.split('.')

    @property
    def version(self):
        """
        Generate a Unique version value from the git information
        :return:
        """
        git_rev = len(os.popen('git rev-list HEAD').readlines())
        if git_rev != 0:
            self.version_list[-1] = '%d' % git_rev
        version = '.'.join(self.version_list)
        return version

    @property
    def branch(self):
        """
        Get the current git branch
        :return:
        """
        return os.popen('git rev-parse --abbrev-ref HEAD').read().strip()

    @property
    def hash(self):
        """
        Return the git hash for the current build
        :return:
        """
        return os.popen('git rev-parse HEAD').read().strip()

    @property
    def origin(self):
        """
        Return the fetch url for the git origin
        :return:
        """
        for item in os.popen('git remote -v'):
            split_item = item.strip().split()
            if split_item[0] == 'origin' and split_item[-1] == '(push)':
                return split_item[1]


def get_and_update_metadata():
    """
    Get the package metadata or generate it if missing
    :return:
    """
    if not os.path.exists('.git') and os.path.exists('hostlists/metadata.json'):
        with open(METADATA_FILENAME) as fh:
            metadata = json.load(fh)
    else:
        git = Git(version=setup_args['version'])
        metadata = {
            'version': git.version
        }
        with open(METADATA_FILENAME, 'w') as fh:
            json.dump(metadata, fh)
    return metadata


if __name__ == '__main__':
    metadata = get_and_update_metadata()
    setup_args['version'] = metadata['version']
    setup(**setup_args)
