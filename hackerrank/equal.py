#!/bin/python3

import math
import operator
import os
import random
import re
import sys
from time import sleep

def min_operations(target, init):
    delta = init - target
    return (delta // 5) + ((delta % 5) // 2) + ((delta % 5) % 2)

def min_operations_until_equal(arr):
    min_value = min(arr)
    min_total_operations = None
    for offset in range(5):
        total_operations = 0
        for x in arr:
            total_operations += min_operations(min_value - offset, x)
        min_total_operations = total_operations if min_total_operations is None\
            else min(min_total_operations, total_operations)
    return min_total_operations

def equal(arr):
    return min_operations_until_equal(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
