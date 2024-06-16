# Binary Search Tree (BST) - Find the maximum value, the minimum value and the sum of values in a BST


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


def find_max_value(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val


def find_min_value(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val


def sum_of_values(root):
    if root is None:
        return 0
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.right = Node(35)

print(root)

max_value = find_max_value(root)
print(f"Maximum value: {max_value}")

min_value = find_min_value(root)
print(f"Minimum value: {min_value}")

total_sum = sum_of_values(root)
print(f"Sum of values: {total_sum}")
