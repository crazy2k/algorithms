import unittest

# O(n**2) time, O(n) space
def urlify(s):
    l = list(s)
    for i in range(len(l)):
        if l[i] == ' ':
            shift(l, i, 2)
            l[i] = '%'
            l[i + 1] = '2'
            l[i + 2] = '0'
    return ''.join(l)


def shift(l, start, offset):
    for i in range(len(l) - 1, start + offset - 1, -1):
        l[i] = l[i - offset]


class Test(unittest.TestCase):
    def test_shift(self):
        l = list("abc   ")
        shift(l, 0, 3)
        self.assertEqual(list("abcabc"), l)

    def test_shift_positive_offset(self):
        l = list("holaabc   ")
        shift(l, 4, 3)
        self.assertEqual(list("holaabcabc"), l)

    def test_urlify(self):
        self.assertEqual("Mr%20John%20Smith", urlify("Mr John Smith    "))
