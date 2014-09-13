def replace_spaces(s):
    s2 = ""
    for c in s:
        if c == " ":
            s2 += "%20"
        else:
            s2 += c
