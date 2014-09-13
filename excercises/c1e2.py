# Since strings in Python are immutable, and the excercises says the
# string is a C-String, I assume the input is a list of characters.
# Also, I take advantage of this to do the reverse in-place.
# Always O(n).
def reverse(l):
    for i in range((len(l) - 1)/2):
        j = (len(l) - 1) - 1 - i
        l[i], l[j] = l[j], l[i]
