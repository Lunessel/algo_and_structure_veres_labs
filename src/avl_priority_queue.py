class Node:
    def __init__(self, value, priority):
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        self.value = value
        self.priority = priority


def get_height(node):
    if node is None:
        return 0
    return node.height


class AVLTree:
    def __init__(self, value, priority):
        self.root = Node(value, priority)

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root
        node.height = 1 + max(get_height(node.left), get_height(node.right))
        new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
        new_root.right = node
        node.parent = new_root
        node.height = 1 + max(get_height(node.left), get_height(node.right))
        new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    def make_balance(self, node):
        while node is not None:
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            node.height = 1 + max(left_height, right_height)
            balance = left_height - right_height
            if balance > 1:
                if get_height(node.left.left) >= get_height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif balance < -1:
                if get_height(node.right.right) >= get_height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
            return
        self.insert_recursion_dfs(self.root, value, priority)
        self.make_balance(self.root)

    def insert_recursion_dfs(self, node, value, priority):
        if priority >= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
                node.left.parent = node
            else:
                self.insert_recursion_dfs(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
                node.right.parent = node
            else:
                self.insert_recursion_dfs(node.right, value, priority)

    def print_tree(self, node):
        if node is not None:
            self.print_tree(node.left)
            print(f'{node.value}({node.priority})')
            self.print_tree(node.right)

    def delete_highest_priority(self):
        current_node = self.root
        if current_node is None:
            return None
        while current_node.left:
            current_node = current_node.left
        deleted_node = (current_node.value, current_node.priority)

        if current_node.right is None:
            current_node.parent.left = None
        else:
            current_node.parent.left = current_node.right

        self.make_balance(current_node.parent)
        return deleted_node
