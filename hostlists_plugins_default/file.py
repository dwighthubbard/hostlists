#!/usr/bin/env python
""" hostlists plugin to get hosts from a filei """

# Copyright (c) 2010-2013 Yahoo! Inc. All rights reserved.
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
import os
from hostlists.plugin_base import HostlistsPlugin


class HostlistsPluginFile(HostlistsPlugin):
    names = ['file']

    def expand(self, value, name="file"):
        tmplist = []
        for host in [
            i.strip() for i in open(os.path.expanduser(value), 'r').readlines()
        ]:
            if not host.startswith('#') and len(host.strip()):
                tmplist.append(host)
        return tmplist
