def longest_inc_subseq(a):
    # `dp[i]` contains the longest increasing subsequence found that ends in
    # `a[i]`
    dp = []
    for i, e in enumerate(a):
        if i == 0:
            dp.append([a[0]])
            continue

        cseqs = [seq for seq in dp if seq[-1] < e]

        maxseq = []
        for seq in cseqs:
            if len(seq) > len(maxseq):
                maxseq = seq

        dp.append(maxseq + [e])

    return max([len(seq) for seq in dp])


if __name__ == '__main__':
    n = int(raw_input())
    a = []
    for c in range(n):
        a.append(int(raw_input()))
    print longest_inc_subseq(a)
