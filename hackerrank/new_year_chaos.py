#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = min_bribes(q)
    if bribes is not None:
        print(bribes)
    else:
        print("Too chaotic")



def min_bribes(q):
    bribers = {}
    bribes = 0
    for _ in range(len(q)):
        prev_bribes = bribes
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                if bribers.get(q[i], 0) <= 1:
                    bribes += 1
                    bribers[q[i]] = bribers.get(q[i], 0) + 1
                    q[i], q[i + 1] = q[i + 1], q[i]
                else:
                    return None
        if bribes == prev_bribes:
            return bribes
                
    return bribes
            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
