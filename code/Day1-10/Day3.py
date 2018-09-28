"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
    
def serialize(node):
    node_str = ''
    li = list()
    preorder_traversal(node, li)
    for ele in li:
        node_str += ele + ' '
    return node_str
    
def preorder_traversal(root, li):
    if root:
        li.append(root.val)
        preorder_traversal(root.left, li)
        preorder_traversal(root.right, li)


def get_index():
    return construct_tree.index

def increment_index():
    construct_tree.index += 1

def construct_tree(arr, low, high, size):
    if low > high or get_index() >= size:
        return None
    
    root = Node(arr[get_index()])
    increment_index()
    j = low
    for i in range(low, high):
        j += 1
        if arr[i] > root.val:
            break

    root.left = construct_tree(arr, get_index(), j - 1, size)
    root.right = construct_tree(arr, j, high, size)

    return root


def deserialize(node_str):
    li = list(node_str.split(' '))
    size = len(li)
    construct_tree.index = 0
    return construct_tree(li, 0, size - 1, size)

    

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    main()

