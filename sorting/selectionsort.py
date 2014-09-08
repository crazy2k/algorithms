def selectionsort(l):
    for i in range(len(l)):
        m = i   # ``m'' is the index of the min
        for j in range(i + 1, len(l)):
            if l[j] < l[m]:
                m = j

        l[i], l[m] = l[m], l[i]
