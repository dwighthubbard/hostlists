#!/usr/bin/env python
# Copyright (c) 2012-2015 Yahoo! Inc. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. See accompanying LICENSE file.
"""
Unit tests of sshmap
"""
import hostlists
import unittest


class TestHostPluginLoad(unittest.TestCase):
    """
    hostmap unit tests
    """
    def setUp(self):
        self.hostlists_plugins = hostlists.installed_plugins()

    def testPluginDnsLoad(self):
        import hostlists.plugins.dns
        self.assertIn('dns', hostlists.plugins.dns.name())
        self.assertIn('dns', self.hostlists_plugins)

    def testPluginDnsIPLoad(self):
        import hostlists.plugins.dnsip
        self.assertIn('dnsip', hostlists.plugins.dnsip.name())
        self.assertIn('dnsip', self.hostlists_plugins)

    def testPluginFileLoad(self):
        import hostlists.plugins.file
        self.assertIn('file', hostlists.plugins.file.name())
        self.assertIn('file', self.hostlists_plugins)

    def testPluginHaproxyLoad(self):
        import hostlists.plugins.haproxy
        self.assertIn('haproxy', hostlists.plugins.haproxy.name())
        self.assertIn('haproxy', self.hostlists_plugins)

    def testPluginRangeLoad(self):
        import hostlists.plugins.range
        self.assertIn('range', hostlists.plugins.range.name())
        self.assertIn('range', self.hostlists_plugins)

if __name__ == '__main__':
    unittest.main()
