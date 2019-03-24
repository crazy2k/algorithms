import unittest


# O(n*m) time, O(n*m) space
def zero_matrix(m):
    zero_rows = set()
    zero_columns = set()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)

    for i in range(len(m)):
        for j in range(len(m[i])):
            if i in zero_rows or j in zero_columns:
                m[i][j] = 0
    return m


class Test(unittest.TestCase):
    def test4by4(self):
        m = [[1, 2, 3, 4],
             [5, 6, 0, 8],
             [9, 10, 11, 12],
             [0, 14, 15, 16]]
        expected = [[0, 2, 0, 4],
                    [0, 0, 0, 0],
                    [0, 10, 0, 12],
                    [0, 0, 0, 0]]
        self.assertEqual(expected, zero_matrix(m))
