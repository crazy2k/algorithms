#!/bin/python3

import os


# Complete the countingValleys function below.
def countingValleys(n, s):
    current_level = 0
    valleys = 0
    for step in s:
        change = -1 if step == "D" else 1
        current_level += change
        if step == "D" and current_level == -1:
            valleys += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
