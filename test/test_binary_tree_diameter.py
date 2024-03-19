import unittest
from src.binary_tree_diameter import binary_tree_diameter, BinaryTree


class TestFindLongestPick(unittest.TestCase):
    def test_given_tree(self):
        root = BinaryTree(20)
        root.insert(22)
        root.insert(10)
        root.insert(11)
        root.insert(12)
        root.insert(13)
        root.insert(9)
        root.insert(8)
        root.insert(7)
        result = binary_tree_diameter(tree=root)
        self.assertEqual(result, 6)

    def test_big_tree(self):
        root = BinaryTree(20)
        root.insert(20)
        root.insert(25)
        root.insert(30)
        root.insert(40)
        root.insert(15)
        root.insert(10)
        root.insert(17)
        root.insert(8)
        root.insert(23)
        root.insert(16)
        root.insert(19)
        root.insert(4)
        root.insert(5)
        root.insert(3)
        root.insert(35)
        root.insert(43)
        root.insert(45)
        result = binary_tree_diameter(tree=root)
        self.assertEqual(result, 10)

    def test_all_left_child_of_tree(self):
        root = BinaryTree(20)
        root.insert(19)
        root.insert(18)
        root.insert(17)
        result = binary_tree_diameter(tree=root)
        self.assertEqual(result, -1)

    def test_all_right_child_of_tree(self):
        root = BinaryTree(20)
        root.insert(21)
        root.insert(22)
        root.insert(23)
        result = binary_tree_diameter(tree=root)
        self.assertEqual(result, -1)

    def test_given_tree_sdf(self):
        root = BinaryTree(100)
        root.insert(50)
        root.insert(120)
        root.insert(105)
        root.insert(125)
        root.insert(10)
        root.insert(8)
        root.insert(6)
        root.insert(5)
        root.insert(12)
        root.insert(15)
        root.insert(18)
        root.insert(19)
        root.insert(20)

        result = binary_tree_diameter(tree=root)
        self.assertEqual(result, 9)


if __name__ == "__main":
    unittest.main()