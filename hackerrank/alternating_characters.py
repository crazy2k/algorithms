def min_changes_to_like(s):
    n = 0
    c = s[0]
    for i in range(1, len(s)):
        if s[i] == c:
            n += 1
        else:
            c = s[i]
    return n

if __name__ == '__main__':
    t = int(raw_input())
    for x in range(t):
        s = raw_input()
        r = min_changes_to_like(s)
        print r
