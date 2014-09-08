import random

def quicksort(l):
    qs(l, 0, len(l) - 1)

def qs(l, begin, end):
    if begin < end:
        p = partition(l, begin, end)
        # After the call to partition(), the pivot is in its final position
        # We only need to sort the rest recursively
        qs(l, begin, p - 1)
        qs(l, p + 1, end)


def partition(l, begin, end):
    # Move the pivot to the end
    p = random.randint(begin, end)
    l[end], l[p] = l[p], l[end]

    i = begin - 1   # Index for last smaller element
    for j in range(begin, end):
        if l[j] <= l[end]:
            i += 1
            l[i], l[j] = l[j], l[i]

    # Put the pivot in its final position
    i += 1
    l[i], l[end] = l[end], l[i]

    return i
