import sys

def min_chars(ws):
    d = set()
    inputs = []
    for w in ws:
        if w not in d:
            d.add(w)
            inputs.append(min_input(w, d))

    return sum([len(i) for i in inputs])

def min_input(w, d):
    for prefix_len in range(1, len(w)):
        prefix = w[:prefix_len]
        matches = {w for w in d if w.startswith(prefix)}
        if len(matches) == 1:
            return prefix
    return w

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as f:
        t = int(f.readline())
        for i in range(1, t + 1):
            n = int(f.readline().strip())
            ws = [f.readline().strip() for x in range(n)]
            r = min_chars(ws)
            print "Case #%d: %d" % (i, r)
