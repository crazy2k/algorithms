def process_buildings(bs, h):
    new_bs = [[0 for f in range(h + 1)] for b in bs]
    for i, b in enumerate(bs):
        for pf in b:
            new_bs[i][pf] += 1
    return new_bs

def max_saved(bs, h, i):
    bs = process_buildings(bs, h)

    dp = [[0 for f in range(h + 1)] for b in bs]
    max_in_f = [0 for f in range(h + 1)]
    for f in range(h + 1):
        for bi in range(len(bs)):
            if f == 1:
                dp[bi][f] = bs[bi][f]
                max_in_f[f] = max(max_in_f[f], dp[bi][f])
            else:
                if f < i:
                    dp[bi][f] = dp[bi][f - 1] + bs[bi][f]
                else:
                    dp[bi][f] = max(dp[bi][f - 1], max_in_f[f - i])
                    dp[bi][f] += bs[bi][f]
                max_in_f[f] = max(max_in_f[f], dp[bi][f])


    return max([dp[bi][h] for bi in range(len(bs))])

if __name__ == '__main__':
    n, h, i = [int(x) for x in raw_input().split()]
    bs = []
    for x in range(n):
        ps = [int(x) for x in raw_input().split()[1:]]
        bs.append(ps)
    print max_saved(bs, h, i)
