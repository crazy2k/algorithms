# Using a dictionary.
# Worst case is ``O(n^2)`` with ``n`` being the number of characters.
def all_unique(s):
    d = {}
    for c in s:
        if c in d:
            return False
        else:
            d[c] = 1
    return True

# Without additional data structures.
# Worst case is ``O(n^2)`` with ``n`` being the number of characters.
def all_unique2(s):
    for i1, c1 in enumerate(s):
        for i2, c2 in enumerate(s):
            if i1 != i2 and c1 == c2:
                return False
    return False
