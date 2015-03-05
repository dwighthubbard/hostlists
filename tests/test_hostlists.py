#!/usr/bin/env python
#Copyright (c) 2012-2015 Yahoo! Inc. All rights reserved.
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

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
import json
import os
import tempfile
import types
import unittest


class TestHostlists(unittest.TestCase):
    """
    hostlists.py unit tests
    """
    def test_cmp_compat(self):
        self.assertEqual(hostlists.cmp_compat(1, 2), -1)
        self.assertEqual(hostlists.cmp_compat(2, 1), 1)

    def test_get_plugins(self):
        plugins = hostlists.get_plugins()
        self.assertIn('file', plugins.keys())
        self.assertIsInstance(plugins['file'], types.ModuleType)

    def test_get_setting_without_config_file(self):
        if os.path.exists('test_get_setting.conf'):
            os.remove('test_get_setting.conf')
        hostlists.hostlists.CONF_FILE = os.path.abspath('test_get_setting.conf')
        result = hostlists.get_setting('key')
        self.assertIsNone(result)

    def test_get_setting_with_config_file(self):
        expected_dict = {
            'key': 'value'
        }
        with open('test_get_setting.conf', 'w') as tf:
            json.dump(expected_dict, tf)
        hostlists.hostlists.CONF_FILE = os.path.abspath('test_get_setting.conf')
        result = hostlists.get_setting('key')
        os.remove('test_get_setting.conf')
        self.assertEqual(result, 'value')

    def test_expand(self):
        """
        Expand a list of lists and set operators into a final host lists
        >>> hostlists.expand(['foo[01-10]','-','foo[04-06]'])
        ['foo09', 'foo08', 'foo07', 'foo02', 'foo01', 'foo03', 'foo10']
        >>>
        """
        result = hostlists.expand(['foo[01-10]','-','foo[04-06]'])
        expected_result = [
            'foo09', 'foo08', 'foo07', 'foo02', 'foo01', 'foo03', 'foo10']
        result.sort()
        expected_result.sort()
        self.assertLessEqual(result, expected_result)

    def test_expand_invalid_plugin(self):
        with self.assertRaises(hostlists.HostListsError) as context:
            result = hostlists.expand(['boozle:bar'])

    def test_expand_file(self):
        with open('test_expand_file.hostlist', 'w') as fh:
            fh.write('foo[1-2]\n')
        result = hostlists.expand(['file:test_expand_file.hostlist'])
        expected_result = ['foo1', 'foo2']
        os.remove('test_expand_file.hostlist')
        result.sort()
        self.assertListEqual(result, expected_result)

    def test_compress(self):
        result = hostlists.compress(['foo1', 'foo3', 'foo4'])
        expected_result = ['foo1', 'foo[3-4]']
        self.assertListEqual(result, expected_result)

    def test_range_split(self):
        result = hostlists.range_split('foo1, foo[3-9]')
        expected_result = ['foo1', ' foo[3-9]']
        self.assertListEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
