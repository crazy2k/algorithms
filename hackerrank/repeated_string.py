#!/bin/python3

import os


# Complete the repeatedString function below.
def repeatedString(s, n):
    if n <= len(s):
        pos = 0
        count = 0
        while pos <= n - 1:
            if s[pos] == "a":
                count += 1
            pos += 1
        return count
                
    time_string_fits = n // len(s)
    count = repeatedString(s, len(s)) * time_string_fits
    rest = n % len(s)
    count += repeatedString(s, rest)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
