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
  described. When one of the pointers reach the end of its associated list, the
  remaining elements in the other list are appended to the third list. Finally,
  the merged list is returned.

  Implementations can be found in `merge_linked_lists.py` (Python) and in the
  `merge_linked_lists_java/` directory (Java).

# Miscellaneous

## URL shortener

* **Question**: How would you implement a URL shortener?

# Trees

## Reverse a tree

* **Question**: Write a function to reverse a binary tree.

# Arrays

## Array with a peak

* **Question**: Given an array such that elements' values increase until a max
  value and then decrease. How would you find the min? And the max? Write
  those functions.
