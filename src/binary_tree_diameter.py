import copy


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

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def binary_tree_diameter(tree: BinaryTree) -> int:
    def dfs(node, length=0):
        nonlocal result
        if node is None:
            return 0
        left_len = dfs(node.left, copy.deepcopy(length)) + 1
        right_len = dfs(node.right, copy.deepcopy(length)) + 1
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
            left_length = max(left_length, right_length)

        tree = tree.parent

    # dfs(tree)
    return result
