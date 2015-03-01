import itertools

def find_longest_palindrome(s):
    global dp
    dp = [[0]*len(s) for x in range(len(s))]
    for r in range(1, len(s) + 1):
        for i in range(len(s) - r + 1):
            j = i + r - 1
            if r == 1:
                dp[i][j] = 1
            elif r == 2:
                dp[i][j] = 2 if s[i] == s[j] else 1
            else:
                third = dp[i + 1][j - 1]
                if s[i] == s[j]:
                    third += 2

                m = max([dp[i + 1][j], dp[i][j - 1], third])
                dp[i][j] = m

def score(s):
    find_longest_palindrome(s)
    scr = 0
    for j in range(len(s) - 1):
        new_scr = dp[0][j]*dp[j + 1][len(s) - 1]
        scr = new_scr if new_scr > scr else scr
    return scr

if __name__ == '__main__':
    s = raw_input()
    print score(s)
