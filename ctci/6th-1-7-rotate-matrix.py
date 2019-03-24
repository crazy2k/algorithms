import unittest


# O(n**2) time, O(n*n) space
def rotate_matrix(m):
    new_m = [[e for e in row] for row in m]

    for level in range(len(m) // 2):
        length = len(m) - level * 2
        for i in range(length):
            new_m[i + level][level + length - 1] = m[level][i + level]
            new_m[level + length - 1][level + length - i - 1] = m[i + level][
                level + length - 1]
            new_m[i + level][level] = m[level + length - 1][i + level]
            new_m[level][i + level] = m[level + length - i - 1][level]
    return new_m


# O(n**2) time, O(n*n) space (constant should be quite lower)
def rotate_matrix_in_place(m):
    for level in range(len(m) // 2):
        length = len(m) - level * 2

        top = [m[level][i + level] for i in range(length)]
        right = [m[i + level][level + length - 1] for i in range(length)]
        bottom = [m[level + length - 1][i + level] for i in range(length)]
        left = [m[level + length - i - 1][level] for i in range(length)]

        for i in range(length):
            m[i + level][level + length - 1] = top[i]
            m[level + length - 1][level + length - i - 1] = right[i]
            m[i + level][level] = bottom[i]
            m[level][i + level] = left[i]
    return m


class Test(unittest.TestCase):
    def test4by4(self):
        m = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        expected = [[13, 9, 5, 1],
                    [14, 10, 6, 2],
                    [15, 11, 7, 3],
                    [16, 12, 8, 4]]
        self.assertEqual(expected, rotate_matrix(m))
        self.assertEqual(expected, rotate_matrix_in_place(m))

    def test5by5(self):
        m = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]]
        expected = [[21, 16, 11, 6, 1],
             [22, 17, 12, 7, 2],
             [23, 18, 13, 8, 3],
             [24, 19, 14, 9, 4],
             [25, 20, 15, 10, 5]]
        self.assertEqual(expected, rotate_matrix(m))
        self.assertEqual(expected, rotate_matrix_in_place(m))
