def find(a, v):
    for i, x in enumerate(a):
        if x == v:
            return i
    return None

if __name__ == '__main__':
    v = int(raw_input())
    n = int(raw_input())
    ar = [int(x) for x in raw_input().split()]

    print find(ar, v)
