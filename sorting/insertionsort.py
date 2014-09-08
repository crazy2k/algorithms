def insertionsort(l):
    for i in range(1, len(l)):
        key = l[i]

        # We have to insert the key in the sorted part. ``j'' is a
        # candidate index for insertion. It will be used if
        # ``key >= l[j - 1]''
        j = i
        while key < l[j - 1] and j >= 1:
            l[j] = l[j - 1]
            j -= 1

        l[j] = key
