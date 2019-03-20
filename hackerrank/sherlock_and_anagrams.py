#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def substrings(s):
    for size in range(1, len(s)):
        for i in range(len(s) - size + 1):
            yield s[i:i + size]

def sherlockAndAnagrams(s):
    anagrams = {}
    for substring in substrings(s):
        key = ''.join(sorted(substring))
        anagrams[key] = anagrams.setdefault(key, 0) + 1

    total = 0
    for n in anagrams.values():
        if n >= 2:
            total += math.factorial(n)/(2 * math.factorial(n - 2))

    return int(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
