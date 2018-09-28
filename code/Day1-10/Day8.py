# -*- coding: utf-8 -*-
"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1


"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def add_left(self, val):
        left = Node(val)
        self.left = left
        return left

    def add_right(self, val):
        right = Node(val)
        self.right = right
        return right


def unival(root, count):
    if root is None:
        return True

    left = unival(root.left, count)
    right = unival(root.right, count)

    if left is False or right is False:
        return False

    if root.left and root.left.val != root.val:
        return False

    if root.right and root.right.val != root.val:
        return False

    count[0] += 1
    return True

def main():
    root = Node(0)
    root.add_left(1)
    right = root.add_right(0)
    node1 = right.add_left(1)
    node1.add_left(1)
    node1.add_right(1)
    right.add_right(0)
    """
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.right = Node(1)
    root.right.left.left = Node(1)
    """
    count = [0]
    unival(root, count)
    print(count[0])


if __name__ == '__main__':
    main()
