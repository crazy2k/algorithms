import sys

def valid_swaps(n):
    k = len(n)

    swaps = [int(n)]
    for i in range(k):
        for j in range(i + 1, k):
            if i == 0 and n[j] == '0':
                continue

            swap = list(n)
            swap[i], swap[j] = swap[j], swap[i]
            swap = ''.join(swap)

            swaps.append(int(swap))

    return swaps

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as f:
        t = int(f.readline())
        for i in range(1, t + 1):
            n = f.readline().strip()
            vs = valid_swaps(n)
            print "Case #%d: %d %d" % (i, min(vs), max(vs))
