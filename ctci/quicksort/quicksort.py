def quicksort(l):
    return quicksort_with_indices(l, 0, len(l) - 1)

def quicksort_with_indices(l, start, end):
    if start < end:
        pivot_idx = partition(l, start, end)
        quicksort_with_indices(l, start, pivot_idx - 1)
        quicksort_with_indices(l, pivot_idx + 1, end)


def partition(l, start, end):
    # Loop invariant: The list is divided in four regions:
    # [(start), ..., (i), ..., (j), ..., (end)]
    # - Elements in [(start), ..., (i)] are less than or equal to l[end]
    # - Elements in [(i + 1), ..., (j - 1)] are greater than l[end].
    # - Elements in [(j), ..., (end - 1)] have no particular relationship to
    #   l[end] 
    # - l[end] is the pivot
    pivot = l[end]  # We can choose a different pivot and swap it to the end
    i = start - 1
    for j in range(start, end + 1):
        if l[j] <= pivot:
            i += 1
            l[j], l[i] = l[i], l[j]
    return i