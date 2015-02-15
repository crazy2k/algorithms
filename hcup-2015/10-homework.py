import sys

def is_prime(n):
    return len(divisors(n)) == 2

def divisors(i):
    return {x for x in range(1, i + 1) if i % x == 0}

def primacity(i):
    return len({d for d in divisors(i) if is_prime(d)})

def question(r, k):
    return len({i for i in r if primacity(i) == k})

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as f:
        t = int(f.readline())
        for i in range(1, t + 1):
            a, b, k = f.readline().strip().split()
            a = int(a)
            b = int(b)
            k = int(k)
            n = question(range(a, b + 1), k)
            print "Case #%d: %d" % (i, n)
