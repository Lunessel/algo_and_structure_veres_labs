class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                    self.left.parent = self
                else:
                    self.left.insert(data)
                    self.left.parent = self

            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                    self.right.parent = self
                else:
                    self.right.insert(data)
                    self.right.parent = self
        else:
            self.data = data


def binary_tree_diameter(tree: BinaryTree) -> int:
    def dfs(node, length=0):
        nonlocal result
        if not node:
            return length

        left_len = dfs(node.left, length + 1)
        right_len = dfs(node.right, length + 1)
        result = max(result, left_len + right_len)

        return left_len if left_len > right_len else right_len

    result = -1
    if tree.left is None:
        return -1
    # get lowest left element
    while tree.left is not None:
        tree = tree.left

    left_length = -1
    while tree is not None:
        left_length += 1
        if tree.right is not None:
            right_length = dfs(tree.right)
            result = max(result, left_length + right_length)

        tree = tree.parent
    return result
