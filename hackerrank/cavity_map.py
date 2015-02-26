def mark_cavities(m):
    newm = [r[:] for r in m]
    n = len(m)
    for i in range(1, n - 1):
        for j in range(1, n -1 ):
            d = m[i][j]
            adjs = [m[i - 1][j], m[i][j + 1], m[i + 1][j], m[i][j - 1]]
            if max(adjs) < d:
                newm[i][j] = "X"
    return newm

if __name__ == '__main__':
    n = int(raw_input())
    m = []
    for x in range(n):
        row = list(raw_input())
        m.append(row)

    mm = mark_cavities(m)
    for row in mm:
        print ''.join(row)
