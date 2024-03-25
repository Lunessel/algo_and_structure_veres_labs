import unittest
from src.min_chess_horse_path import find_min_chess_horse_path_and_length


class TestFindLongestPick(unittest.TestCase):
    def test_given_input_data(self):
        find_min_chess_horse_path_and_length(input_file_name='given_input.txt', output_file_name='given_output.txt')
        file = open("../resources/given_output.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 6)

    def test_empty_input_data(self):
        find_min_chess_horse_path_and_length(input_file_name='empty_input.txt', output_file_name='empty_output.txt')
        file = open("../resources/empty_output.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, -1)



if __name__ == "__main":
    unittest.main()
