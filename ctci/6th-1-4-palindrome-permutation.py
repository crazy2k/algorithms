import unittest
from collections import Counter


def palindrome_permutation(s):
    processed = [c.lower() for c in s if c != ' ']
    counter = Counter(processed)
    single_chars = 0
    for k in counter:
        if counter[k] > 2:
            return False
        if counter[k] == 1:
            single_chars += 1
    return len(processed) % 2 == 0 and single_chars == 0 or \
           len(processed) % 2 == 1 and single_chars == 1


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(palindrome_permutation("Tact Coa"))
        self.assertTrue(palindrome_permutation("abba"))
        self.assertTrue(palindrome_permutation("baba"))
        self.assertTrue(palindrome_permutation("babza"))
        self.assertFalse(palindrome_permutation("aaab"))
