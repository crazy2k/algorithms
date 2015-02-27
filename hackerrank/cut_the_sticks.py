def cut_sticks(sticks):
    cut = []
    while len(sticks):
        cut.append(len(sticks))
        min_stick = min(sticks)
        sticks = [s - min_stick for s in sticks if s - min_stick > 0]
    return cut

if __name__ == '__main__':
    n = int(raw_input())
    sticks = map(int, raw_input().split())
    r = cut_sticks(sticks)
    for c in r:
        print c
