import itertools

pal_table = {}
def is_palindrome(w):
    if w in pal_table:
        return pal_table[w]
    for i in range(len(w)/2 + 1):
        if w[i] != w[len(w) - 1 - i]:
            pal_table[w] = False
            return False
    pal_table[w] = True
    return True

largest_pal = {}
def find_largest_palindrome(s, i, j):
    subs = s[i:j + 1]
    if subs in largest_pal:
        return largest_pal[subs]
    for r in range(len(subs), -1, -1):
        for subsubs in itertools.combinations(subs, r):
            if is_palindrome(subsubs):
                largest_pal[subs] = len(subsubs)
                return len(subsubs)
    largest_pal[subs] = 0
    return 0

def score(s):
    scr = 0
    for a_i in range(len(s) - 1):
        for a_j in range(a_i, len(s) - 1):
            for b_i in range(a_j + 1, len(s)):
                for b_j in range(b_i, len(s)):
                    p1 = find_largest_palindrome(s, a_i, a_j)
                    p2 = find_largest_palindrome(s, b_i, b_j)
                    new_scr = p1*p2
                    scr = new_scr if new_scr > scr else scr
    return scr


if __name__ == '__main__':
    s = raw_input()
    print score(s)
