def int_to_sbin(n):
    s = ""
    for x in range(32):
        b = "1" if n & 1 else "0"
        s = b + s
        n = n >> 1
    return s

def flip_bits(n):
    s = int_to_sbin(n)
    l = list(s)
    flipped_l = ['1' if b == '0' else '0' for b in l]
    flipped_s = ''.join(flipped_l)
    return int(flipped_s, 2)

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        r = flip_bits(n)
        print r
