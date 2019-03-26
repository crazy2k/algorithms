import unittest


def remove_node(l, prev_node, node):
    if prev_node == None:
        l.first = node.next
    else:
        prev_node.next = node.next

def remove_dups(l):
    seen = set()
    prev_node = None
    node = l.first
    while node is not None:
        if node.data in seen:
            remove_node(l, prev_node, node)
        

class LinkedList:
    def __init__(self, first):
        self.first = first
        
    def __eq__(self, other):
        return other is not None and self.first == other.first

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __eq__(self, other):
        print(self, other)
        return other is not None and self.data == other.data and self.next == other.next

    def __repr__(self):
        return 'Node(%s, %s)' % (self.data, self.next)


class Test(unittest.TestCase):
    def test(self):
        l = LinkedList(Node(1, Node(2, Node(2, None))))
        remove_dups(l)
        expected = LinkedList(Node(1, Node(2, None)))
        self.assertEqual(expected, l)
