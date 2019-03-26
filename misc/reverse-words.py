import unittest


def reverse_sublist(l, start, end):  # [abc def]
    for i in range((end - start + 1) // 2):
        l[start + i], l[end - i] = l[end - i], l[start + i]


def reverse_words_in_list(l):
    start = None
    for i in range(len(l)):
        if l[i] != ' ' and start is None:
            start = i
        elif l[i] == ' ' and start is not None:
            reverse_sublist(l, start, i - 1)
            start = None
    if start is not None:
        reverse_sublist(l, start, len(l) - 1)


def reverse_words(l):
    reverse_sublist(l, 0, len(l) - 1)
    reverse_words_in_list(l)


class Test(unittest.TestCase):
    def test_long_words(self):
        l = list('practice makes perfect')
        reverse_words(l)
        self.assertEqual('perfect makes practice', ''.join(l))

    def test_one_char_words(self):
        l = list('a b c')
        reverse_words(l)
        self.assertEqual('c b a', ''.join(l))

    def test_initial_spaces(self):
        l = list('    ab cd ef')
        reverse_words(l)
        self.assertEqual('ef cd ab    ', ''.join(l))
