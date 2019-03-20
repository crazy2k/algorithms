#!/bin/python3

import os


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position = 0
    steps = 0
    while position < len(c) - 1:
        if position < len(c) - 2 and c[position + 2] != 1:
            position += 2
        else:
            position += 1
        steps += 1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
