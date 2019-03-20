#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = {}
    for word in magazine:
        magazine_dict[word] = magazine_dict.setdefault(word, 0) + 1

    for word_in_note in note:
        if word_in_note in magazine_dict and magazine_dict[word_in_note] > 0:
            magazine_dict[word_in_note] -= 1
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
