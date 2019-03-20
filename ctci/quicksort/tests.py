import unittest
from ctci.quicksort import quicksort

class TestQuicksort(unittest.TestCase):

    def test_partition_simple(self):
        l = [2, 8, 7, 1, 3, 5, 6, 4]
        pivot_idx = quicksort.partition(l, 0, len(l) - 1)
        left_region = l[:pivot_idx]
        right_region = l[pivot_idx + 1:]
        self.assertTrue(all(x <= l[pivot_idx] for x in left_region))
        self.assertTrue(all(x > l[pivot_idx] for x in right_region))
        
    def test_quicksort_simple(self):
        l = [2, 8, 7, 1, 3, 5, 6, 4]
        quicksort.quicksort(l)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], l)

if __name__ == '__main__':
    unittest.main()