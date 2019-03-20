def common_elements_1(a1, a2):
    s1 = set(a1)
    s2 = set(a2)
    return s1.intersection(s2)

def common_elements_2(a1, a2):
    # ordenar y despues ir recorriendo es n*log(n) + n
    # 