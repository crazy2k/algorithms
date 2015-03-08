def longest_common_subsequence(a, n, b, m):
    if n == 0 or m == 0:
        return []
    if a[n - 1] == b[m - 1]:
        return longest_common_subsequence(a, n - 1, b, m - 1) + [a[n - 1]]
    l = longest_common_subsequence(a, n, b, m - 1)
    r = longest_common_subsequence(a, n - 1, b, m)
    return l if len(l) > len(r) else r


if __name__ == '__main__':
    n, m = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    b = [int(x) for x in raw_input().split()]
    print longest_common_subsequence(a, len(a), b, len(b))
