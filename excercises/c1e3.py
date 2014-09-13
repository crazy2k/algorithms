# Strings are represented as a list of characters with "END"
# representing the null character.
# O(n^2) with ``n`` being the number of characters
def remove_duplicates(l):
    i1 = 0
    while l[i1] != "END":
        i2 = 0
        while l[i2] != "END":
            if i1 != i2 and l[i1] == l[i2]:
                remove_element(l, i2)
            i2 += 1
        i1 += 1

def remove_element(l, i):
    j = i
    while l[j] != "END":
        l[j] = l[j + 1]
        j += 1
