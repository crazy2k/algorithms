def binary_search(l, i, j, e):
    while i <= j:
        k = (j - i)/2 + i
        if e < l[k]:
            j = k - 1
        elif e > l[k]:
            i = k + 1
        else:
            return k
    return i

def longest_inc_subseq(a):
    # `dp[i]` contains the length of the longest increasing subsequence found
    # that ends in `a[i]`
    dp = [1 for x in a]
    # `min_tail_for_lis[i]` represents the minimum tail for the LIS of size
    # `i`
    min_tail_for_lis = [0]
    for i, e in enumerate(a):
        # First iteration. LIS is always 1
        if i == 0:
            dp[0] = 1
            s = 1
            min_tail_for_lis.append(a[i])
        # If `a[i]` is less than the `min_tail_lis[1]`, then we have a LIS of
        # size 1 with a lower tail and the only LIS that ends in `a[i]` has to
        # be `a[i]` itself
        elif a[i] < min_tail_for_lis[1]:
            min_tail_for_lis[1] = a[i]
            dp[i] = 1
        # If `a[i]` is greater than `min_tail_for_lis` for the current LIS
        # size, then we have a new LIS
        elif a[i] > min_tail_for_lis[-1]:
            min_tail_for_lis.append(a[i])
            dp[i] = len(min_tail_for_lis) - 1
        # Else, `a[i]` is less than or equal to the `min_tail_for_lis` for
        # current LIS. In that case, we have to find a place for it in the
        # `min_tail_for_lis`, as there
        else:
            j = len(min_tail_for_lis) - 1
            # `k` will be the index of the first greater or equal number to
            # `a[i]` in `min_tail_for_lis`
            k = binary_search(min_tail_for_lis, 0, j, a[i])
            min_tail_for_lis[k] = a[i]
            dp[i] = k

    return len(min_tail_for_lis) - 1


if __name__ == '__main__':
    n = int(raw_input())
    a = []
    for c in range(n):
        a.append(int(raw_input()))
    print longest_inc_subseq(a)
