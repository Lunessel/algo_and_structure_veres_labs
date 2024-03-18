import unittest
from src.avl_priority_queue import Node, AVLTree


class TestFindLongestPick(unittest.TestCase):
    def test_delete_max_priority_function(self):
        root = AVLTree(1, 1)
        root.insert(1.5, 0.1)
        root.insert(2, 1)
        root.insert(3, 1)
        root.insert(2, 2.5)
        root.insert(3, 3)
        root.insert(4.3, 4)

        self.assertEqual(root.delete_highest_priority(), (4.3, 4))

    def test_equal_priority_input_data(self):
        root = AVLTree(1, 1)
        root.insert(2, 1)
        root.insert(3, 1)
        root.insert(4, 1)
        root.insert(5, 1)

        self.assertEqual(root.root.left.value, 2)

    def test_increasing_priority_input_data(self):
        root = AVLTree(1, 1)
        root.insert(11, 2)
        root.insert(111, 3)
        root.insert(1111, 4)
        root.insert(11111, 5)

        self.assertEqual(root.root.left.value, 11)


if __name__ == "__main":
    unittest.main()
