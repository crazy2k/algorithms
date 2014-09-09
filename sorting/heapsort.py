heapsize = 0
def build_max_heap(l):
    global heapsize

    heapsize = len(l)
    # Indices ``len(l)/2'' to ``len(l) - 1'' are leaves
    for i in range(len(l)/2 - 1, -1, -1):
        max_heapify(l, i)

def max_heapify(l, i):
    global heapsize

    # We assume that left and right subtrees are max-heaps
    lc = left(i)
    rc = right(i)

    # ``m'' will be the largest element of the three
    m = i
    if lc < heapsize and l[lc] > l[i]:
        m = lc
    if rc < heapsize and l[rc] > l[m]:
        m = rc

    if m != i:
        l[i], l[m] = l[m], l[i]
        # We need to make sure the new subtree rooted at ``m'' is a
        # max-heap
        max_heapify(l, m)

def heapsort(l):
    global heapsize

    build_max_heap(l)
    for i in range(len(l) - 1):
        # Put the largest element at the back
        l[0], l[heapsize - 1] = l[heapsize - 1], l[0]
        # Exclude that element from the heap
        heapsize -= 1
        # Heapify with new root
        max_heapify(l, 0)
    

def parent(i):
    return i/2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1



