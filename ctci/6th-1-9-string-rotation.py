import unittest


def string_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 * 2


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(string_rotation("water", "water"))
        self.assertTrue(string_rotation("water", "aterw"))
        self.assertTrue(string_rotation("water", "terwa"))
        self.assertTrue(string_rotation("water", "erwat"))
        self.assertTrue(string_rotation("water", "rwate"))
        self.assertTrue(string_rotation("water", "aterw"))
        self.assertFalse(string_rotation("water", ""))
        self.assertFalse(string_rotation("water", "waterw"))
        self.assertFalse(string_rotation("water", "watera"))
        self.assertFalse(string_rotation("water", "watea"))
