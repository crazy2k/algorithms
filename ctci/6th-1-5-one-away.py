import unittest


def one_replace_away(s1, s2):
    if len(s1) != len(s2):
        return False
    replaces_needed = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            replaces_needed += 1
    return replaces_needed == 1


def one_insertion_away(s1, s2):
    if len(s2) < len(s1):
        s1, s2 = s2, s1
    adds = 0
    for i in range(len(s2)):
        if i - adds >= len(s1) or s1[i - adds] != s2[i]:
            adds += 1
    return len(s1) + adds == len(s2) and adds in [0, 1]


def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 2:
        return False
    return one_insertion_away(s1, s2) or one_replace_away(s1, s2)


class Test(unittest.TestCase):
    def test(self):
        def test_strings(s1, s2, assertion):
            assertion(one_away(s1, s2))
            assertion(one_away(s2, s1))

        test_strings('pale', 'ple', self.assertTrue)
        test_strings('pales', 'pale', self.assertTrue)
        test_strings('pale', 'bale', self.assertTrue)
        test_strings('pale', 'baje', self.assertFalse)
