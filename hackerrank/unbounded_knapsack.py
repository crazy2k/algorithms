def knapsack_total(a, k):
    r = [0 for x in range(k + 1)]
    for goal in range(1, k + 1):
        if goal == 1:
            r[goal] = goal if goal in a else 0
            continue

        if goal in a:
            r[goal] = goal
        else:
            p = [r[i] + r[goal - i] for i in range(1, goal)]
            r[goal] = max(p)
    return r[k]

if __name__ == '__main__':
    t = int(raw_input())
    for tc in range(t):
        n, k = [int(x) for x in raw_input().split()]
        a = [int(x) for x in raw_input().split()]
        print knapsack_total(a, k)
