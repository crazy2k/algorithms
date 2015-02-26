def max_xor(l):
    m = 0
    for i, x in enumerate(l):
        for j in range(i, len(l)):
            xored = l[i] ^ l[j]
            m = xored if xored > m else m
    return m

if __name__ == '__main__':
    l = int(raw_input())
    r = int(raw_input())
    r = max_xor(range(l, r + 1))
    print r
