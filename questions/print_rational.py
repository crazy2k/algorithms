def div2rational(n, m):
    prev = []
    s = []
    while True:
        if n in prev:
            i = prev.index(n) + 1
            s = s[:i] + ["("] + s[i:] + [")"]
            break
        if n == 0:
            break

        prev.append(n)

        if n < m:
            s.append("0")
            if len(prev) == 1:
                s.append(".")
            n = n*10
        else:
            d = n/m
            r = n % m
            s.append(str(d))
            n = r*10

    return "".join(s)

if __name__ == "__main__":
    print div2rational(1, 3)
    print div2rational(1, 5)
    print div2rational(12, 99)
    print div2rational(12, 99)
    print div2rational(1, 999)
    print div2rational(1, 8)
    print div2rational(1001, 10000)
