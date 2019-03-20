import unittest


def check_permutation(s1, s2):
    seen = {}
    for x in s1:
        seen[x] = seen.setdefault(x, 0) + 1

    for x in s2:
        if x in seen:
            seen[x] -= 1
            if seen[x] == 0:
                del seen[x]
        else:
            return False
    return len(seen) == 0


class Test(unittest.TestCase):
    def test_permutation(self):
        strings = ["hola", "ohla"]
        self.assertTrue(check_permutation(*strings))
        self.assertTrue(check_permutation(*reversed(strings)))
        
    def test_repeated_chars(self):
        strings = ["foobar", "ofobra"]
        self.assertTrue(check_permutation(*strings))
        self.assertTrue(check_permutation(*reversed(strings)))
        
    def test_no_permutation(self):
        strings = ["foobar", "echo"]
        self.assertFalse(check_permutation(*strings))
        self.assertFalse(check_permutation(*reversed(strings)))

    def test_partial_permutation(self):
        strings = ["foobar", "foobaz"]
        self.assertFalse(check_permutation(*strings))
        self.assertFalse(check_permutation(*reversed(strings)))

    def test_same_chars_different_times(self):
        strings = ["foo", "fo"]
        self.assertFalse(check_permutation(*strings))
        self.assertFalse(check_permutation(*reversed(strings)))

if __name__ == '__main__':
    unittest.main()
