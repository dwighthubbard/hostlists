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

import setuptools
from setuptools import setup
import sys


def setuptools_version_supported():
    major, minor, patch = setuptools.__version__.split('.')
    if int(major) > 34:
        return True
    return False


if __name__ == '__main__':
    if not setuptools_version_supported():
        print('Setuptools version 34.0.0 or higher is needed to install this package')
        sys.exit(1)
    setup()
