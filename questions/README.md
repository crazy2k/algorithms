# Lists

* *Given two singly-linked lists, whose elements are in ascending order, write
  a `merge()` function that takes both lists and creates a third with all the
  elements of the former lists in ascending order.*

  The idea here is to create a new empty list and have two pointers, each to the
  head of each input list. At first, both elements in the heads are compared.
  Suppose that the head of the first list has the lower element. Then, that
  element is appended to the newly-created list and the first pointer is
  advanced to the second element in the list it's pointing to. The case when the
  lower element is pointed by the second pointer is analogous to the case just
  described.
  
  When one of the pointers reach the end of its associated list, the remaining
  elements in the other list are appended to the third list. Finally, the
  merged list is returned.

  Implementations can be found in `merge_linked_lists.py` (Python) and in the
  `merge_linked_lists_java/` directory (Java).


# Math

* *Write a function `print_rational(n, m)` that returns a string with the
  rational number resulting of dividing integer `n` over integer `m`. Also, in
  cases where a string of digits repeats itself in the result, find a way to
  stop the algorithm and show the repeating sequence; for example:
  `print_rational(12, 99)` could return `0.(12)`.*

  First, let's think how the division algorithm works in this situation. If we
  want to divide `1/4`, for example, what do we do? We could start by adding a
  `0.` to the result and multiply `n` by 10. Then solve the division `10/4`.
  And how do we solve that? Well, `10 = 4*2 + 2`, so we could add `2` to the
  result and then divide `20/4` (`20 = 2*10`). And that's easy: `20 = 4*5` and
  there's no remainder, so we can stop.

  At first glance, this looks a lot like a recursive problem. Here's an idea:

    def div2rational(n, m):
        if n < m:
            return "0" + div2rational(n*10, m)
        if n >= m:
            d = n/m # integer division
            r = n % m
            return str(d) + div2rational(r*10, m)



# Miscellaneous

* *How would you implement a URL shortener?*

# Trees

## Reverse a tree

* **Question**: Write a function to reverse a binary tree.

# Arrays

## Array with a peak

* **Question**: Given an array such that elements' values increase until a max
  value and then decrease. How would you find the min? And the max? Write
  those functions.
