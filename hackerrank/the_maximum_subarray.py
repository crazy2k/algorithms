#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.

def max_subarray_sum(arr):
    res = last_max_subarray_sum = arr[0]
    for end in range(1, len(arr)):
        last_max_subarray_sum = max(last_max_subarray_sum + arr[end], arr[end])
        res = max(res, last_max_subarray_sum)
    return res

def max_subsequence(arr):
    positives = [x for x in arr if x > 0]
    return sum(positives) if len(positives) > 0 else max(arr)


def maxSubarray(arr):
    return [max_subarray_sum(arr), max_subsequence(arr)]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
