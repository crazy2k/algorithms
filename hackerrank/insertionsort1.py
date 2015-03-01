def pseudo_insertionsort(a):
    def print_arr(arr):
        print " ".join([str(x) for x in arr])

    j = len(a) - 1
    v = a[j]
    i = j
    while i >= 1 and a[i - 1] > v:
        a[i] = a[i - 1]
        i -= 1
        print_arr(a)
    a[i] = v
    print_arr(a)

if __name__ == '__main__':
    s = int(raw_input())
    ar = [int(x) for x in raw_input().split()]
    pseudo_insertionsort(ar)
