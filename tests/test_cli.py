import sys
import unittest
from hostlists.cli import parse_arguments


class TestCLI(unittest.TestCase):
    argv_orig = None

    def setUp(self):
        self.argv_orig = sys.argv

    def tearDown(self):
        if self.argv_orig:
            sys.argv = self.argv_orig
            self.argv_orig = None

    def test__parse_arguments__defaults(self):
        with self.assertRaises(SystemExit):
            result = parse_arguments()

    def test__parse_arguments__hostrange__single(self):
        sys.argv = ['hostlists', 'test[1-2].yahoo.com']
        result = parse_arguments()
        self.assertIsInstance(result.host_range, list)
        self.assertEqual(len(result.host_range), 1)
        self.assertListEqual(result.host_range, ['test[1-2].yahoo.com'])
