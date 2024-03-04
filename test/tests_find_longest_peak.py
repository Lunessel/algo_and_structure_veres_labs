import unittest
from src.find_longest_peak import *


class TestFindLongestPick(unittest.TestCase):
    def test_given_array(self):
        result = find_longest_peak([1, 3, 5, 4, 2, 8, 3, 7])
        self.assertEqual(result, 5)

    def test_sorted_array(self):
        result = find_longest_peak([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(result, -1)

    def test_pick_with_double_same_value(self):
        result = find_longest_peak([1, 2, 6, 6, 3])
        self.assertEqual(result, -1)

    def test_single_element_array(self):
        result = find_longest_peak([2])
        self.assertEqual(result, -1)

    def test_single_elementsd_array(self):
        result = find_longest_peak([1, 2, 7, 8, 6, 4, 2, 5, 6, 7, 9, 11, 12, 17, 9])
        self.assertEqual(result, 9)


if __name__ == "__main":
    unittest.main()
