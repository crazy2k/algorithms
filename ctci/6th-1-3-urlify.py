import unittest


# O(n**2) time, O(n) space
def urlify(l):
    for i in range(len(l)):
        if l[i] == ' ':
            shift(l, i, 2)
            l[i] = '%'
            l[i + 1] = '2'
            l[i + 2] = '0'


def shift(l, start, offset):
    for i in range(len(l) - 1, start + offset - 1, -1):
        l[i] = l[i - offset]


# O(n) time, O(n) space
def urlify2(l):
    def get_true_length(l):
        for i in range(len(l) - 1, -1, -1):
            if l[i] != ' ':
                return i + 1

    def get_true_spaces(l, true_length):
        return sum(1 if l[i] == ' ' else 0 for i in range(true_length))

    true_length = get_true_length(l)
    spaces = get_true_spaces(l, true_length)
    j = true_length - 1 + spaces * 2

    for i in range(true_length - 1, -1, -1):
        if l[i] != ' ':
            l[j] = l[i]
            j -= 1
        else:
            l[j] = '0'
            l[j - 1] = '2'
            l[j - 2] = '%'
            j -= 3


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
        l = list("Mr John Smith    ")
        urlify(l)
        self.assertEqual(list("Mr%20John%20Smith"), l)
        l = list("Mr John Smith    ")
        urlify2(l)
        self.assertEqual(list("Mr%20John%20Smith"), l)
