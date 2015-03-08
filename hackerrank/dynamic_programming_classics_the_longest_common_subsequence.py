def longest_common_subsequence(a, b):
    n = len(a)
    m = len(b)
    dp = [[[] for x in range(m + 1)] for y in range(n + 1)]
    for misum in range(n + m + 1):
        xmax = min(misum, n)
        for x in range(xmax + 1):
            y = misum - x
            if y > m:
                continue

            if x == 0 or y == 0:
                dp[x][y] = []
            elif a[x - 1] == b[y - 1]:
                dp[x][y] = dp[x - 1][y - 1] + [a[x - 1]]
            else:
                l = dp[x - 1][y]
                r = dp[x][y - 1]
                dp[x][y] = l if len(l) > len(r) else r
    return dp[n][m]

if __name__ == '__main__':
    n, m = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    b = [int(x) for x in raw_input().split()]
    lcs = " ".join([str(x) for x in longest_common_subsequence(a, b)])
    print lcs
