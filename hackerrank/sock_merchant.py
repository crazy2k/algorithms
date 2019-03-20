#!/bin/python3

import os

# Complete the sockMerchant function below.
from collections import Counter


def sockMerchant(n, ar):
    counter = Counter()
    for color in ar:
        counter[color] += 1
    
    pairs = 0
    for count in counter.values():
        pairs += count//2
    return pairs
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

