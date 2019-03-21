import unittest
from collections import Counter


def compress(s):
    l = []
    last = s[0]
    count = 1
    for x in s[1:]:
        if x == last:
            count += 1
        else:
            l.append(last)
            l.append(str(count))
            last = x
            count = 1

    l.append(last)
    l.append(str(count))

    return ''.join(l) if len(l) < len(s) else s


class Test(unittest.TestCase):
    def test_compress(self):
        self.assertEqual('a2b1c5a3', compress('aabcccccaaa'))
        self.assertEqual('abcaa', compress('abcaa'))