def insertionsort(a):
    c = 0
    for j in range(1, len(a)):
        v = a[j]
        i = j
        while i >= 1 and a[i - 1] > v:
            a[i] = a[i - 1]
            i -= 1
            c += 1
        a[i] = v
    print c

if __name__ == '__main__':
    s = int(raw_input())
    ar = [int(x) for x in raw_input().split()]
    insertionsort(ar)
