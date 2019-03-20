#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    indices = {}
    for i in range(len(arr)):
        indices[arr[i]] = indices.setdefault(arr[i], []) + [i]

    triplets = 0
    for i in range(len(arr)):
        second = arr[i] * r
        third = second * r
        for second_index in indices.setdefault(second, []):
            if second_index > i:
                for third_index in indices.setdefault(third, []):
                    if third_index > second_index:
                        triplets += 1
    return triplets


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
