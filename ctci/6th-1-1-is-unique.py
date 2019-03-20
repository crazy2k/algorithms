# No restrictions
# O(n) time, O(n) space
def is_unique(s):
    seen = set()
    for x in s:
        if x in s:
            return False
        seen.add(x)
    return True


# Without additional data structures
# O(n**2) time, O(n) space
def is_unique_no_data_structures(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# Sorting
# O(n*log(n)) time, O(n) space
def is_unique_with_sorting(s):
    s = sorted(s)
    for i in range(len(s)):
        if s[i] == s[i + 1]:
            return False
    return True
