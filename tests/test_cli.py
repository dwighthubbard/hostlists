import sys
import unittest
from hostlists.cli import main, parse_arguments


class TestCLI(unittest.TestCase):
    argv_orig = None

    def setUp(self):
        self.argv_orig = sys.argv

    def tearDown(self):
        if self.argv_orig:
            sys.argv = self.argv_orig
            self.argv_orig = None

    def test__parse_arguments__list_plugins(self):
        sys.argv = ['hostlists', '--list_plugins']
        result = parse_arguments()
        self.assertTrue(result.list_plugins)

    def test__parse_arguments__list_plugins_short(self):
        sys.argv = ['hostlists', '-l']
        result = parse_arguments()
        self.assertTrue(result.list_plugins)

    def test__parse_arguments__hostrange__single(self):
        sys.argv = ['hostlists', 'test[1-2].yahoo.com']
        result = parse_arguments()
        self.assertIsInstance(result.host_range, list)
        self.assertEqual(len(result.host_range), 1)
        self.assertListEqual(result.host_range, ['test[1-2].yahoo.com'])

    def test__parse_arguments__expand__default(self):
        sys.argv = ['hostlists', '-e', 'test[1-2].yahoo.com']
        result = parse_arguments()
        self.assertIsInstance(result.host_range, list)
        self.assertEqual(len(result.host_range), 1)
        self.assertListEqual(result.host_range, ['test[1-2].yahoo.com'])
        self.assertTrue(result.expand)
        self.assertEqual(result.sep, '\n')

    def test__parse_arguments__expand__sep(self):
        sys.argv = ['hostlists', '-e', '-s', ',', 'test[1-2].yahoo.com']
        result = parse_arguments()
        self.assertIsInstance(result.host_range, list)
        self.assertEqual(len(result.host_range), 1)
        self.assertListEqual(result.host_range, ['test[1-2].yahoo.com'])
        self.assertTrue(result.expand)
        self.assertEqual(result.sep, ',')
