def mergesort(l):
    ms(l, 0, len(l) - 1)

def ms(l, begin, end):
    if begin < end:
        middle = (end + begin)/2    # An integer here means floor

        ms(l, begin, middle)
        ms(l, middle + 1, end)
        merge(l, begin, middle, end)

def merge(l, begin, middle, end):
    merged = range(end - begin + 1)
    i = begin
    j = middle + 1
    k = 0
    while i <= middle and j <= end:
        if l[i] < l[j]:
            merged[k] = l[i]
            i += 1
        else:
            merged[k] = l[j]
            j += 1

        k += 1

    if i > middle:
        while j <= end:
            merged[k] = l[j]
            j += 1
            k += 1
    else:
         while i <= middle:
            merged[k] = l[i]
            i += 1
            k += 1

    i = begin
    for x in range(len(merged)):
        l[i] = merged[x]
        i += 1
