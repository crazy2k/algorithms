def insertionsort(a):
    def print_arr(arr):
        print " ".join([str(x) for x in arr])

    for j in range(1, len(a)):
        v = a[j]
        i = j
        while i >= 1 and a[i - 1] > v:
            a[i] = a[i - 1]
            i -= 1
        a[i] = v
        print_arr(a)

if __name__ == '__main__':
    s = int(raw_input())
    ar = [int(x) for x in raw_input().split()]
    insertionsort(ar)
