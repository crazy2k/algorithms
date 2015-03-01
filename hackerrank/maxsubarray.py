if False:
    def max_c_ending_in(a, j):
        if j == 0:
            return a[j]
        return max(max_c_ending_in(a, j - 1) + a[j], a[j])

    def max_c(a):
        return max([max_c_ending_in(a, j) for j in range(len(a))])

    def max_nc_until(a, j):
        if j == 0:
            return a[j]
        return max(max_nc_until(a, j - 1), max_nc_until(a, j - 1) + a[j], a[j])

    def max_nc(a):
        return max_nc_until(a, len(a) - 1)

def max_nc(a):
    dp = []
    for j in range(len(a)):
        if j == 0:
            dp.append(a[j])
        else:
            dp.append(max(dp[j - 1], dp[j -1] + a[j], a[j]))
    return dp[len(a) - 1]


def max_c(a):
    dp = []
    for j in range(len(a)):
        if j == 0:
            dp.append(a[j])
        else:
            dp.append(max(dp[j - 1] + a[j], a[j]))
    return max(dp)

if __name__ == '__main__':
    t = int(raw_input())
    for c in range(t):
        n = int(raw_input())
        a = [int(x) for x in raw_input().split()]
        mc = max_c(a)
        mnc = max_nc(a)
        print "%d %d" % (mc, mnc)
