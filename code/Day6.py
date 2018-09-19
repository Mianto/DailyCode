"""
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node.
Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

"""
# Can't be solved as Python doesn't allow to change the address of the pointer
# https://stackoverflow.com/questions/46401486/how-to-implement-an-xor-linked-list-in-python
# More about Data Structure on https://en.wikipedia.org/wiki/XOR_linked_list
class Node:
    def __init__(self, value, prev, next):
        self.val = value
        self.both = prev ^ next


def add(head, element):
    pass

def get(index):
    pass
