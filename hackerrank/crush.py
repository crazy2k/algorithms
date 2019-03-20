#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*n
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    current_sum = 0
    max_value = 0
    for x in arr:
        current_sum += x
        max_value = max(max_value, current_sum)
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
