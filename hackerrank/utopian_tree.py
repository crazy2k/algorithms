def utopian_height(initial_h, n):
    h = initial_h
    spring = True
    for x in range(n):
        h = h*2 if spring else h + 1
        spring = not spring
    return h

if __name__ == '__main__':
    t = int(raw_input())
    for x in range(t):
        n = int(raw_input())
        r = utopian_height(1, n)
        print r
