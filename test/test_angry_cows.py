import unittest
from src.angry_cows import get_max_width


class TestFindLongestPick(unittest.TestCase):
    def test_given_array(self):
        result = get_max_width(cows=3, free_sections=[1, 2, 8, 4, 9])
        self.assertEqual(result, 3)

    def test_sorted_array(self):
        result = get_max_width(cows=4, free_sections=[1, 2, 8, 15, 22])
        self.assertEqual(result, 7)

    def test_pick_with_double_same_value(self):
        result = get_max_width(cows=4, free_sections=[1, 2, 3, 4, 5, 10, 30, 40, 60, 90])
        self.assertEqual(result, 29)


if __name__ == "__main":
    unittest.main()
