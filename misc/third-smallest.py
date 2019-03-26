# Given a set of ints, return the third smallest element
import unittest


def third_smallest(s):
    if len(s) < 3:
        return None

    three_smallest = []
    for x in s:
        three_smallest.append(x)
        three_smallest.sort()
        three_smallest = three_smallest[:3]
    return three_smallest[2]


class Test(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(3, third_smallest({2, 1, 5, 4, 3}))
        self.assertEqual(None, third_smallest({1, 2}))
