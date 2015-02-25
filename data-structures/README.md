A dynamic set is the computational idea of a mathematical set. A dynamic set
can change over time: Its elements can be changed, and elements can be added
or deleted from it, so the size of the set can change too. Usually, every
element in the dynamic set has an associated identifying key.

There are some interesting operations related to dynamic sets that, in some
bibliography, are called "dictionary operations". These operations are the
following:

* **Search**: Given a dynamic set `S` and a key `k`, retrieve the element
  whose key is `k`.
* **Insert**: Given a dynamic set `S` and an element `x`, insert the element
  `x` in the dynamic set `S`.
* **Delete**: Given a dynamic set `S` and an element `x`, remove the element
  `x` from the dynamic set `S`.

# Direct-address tables

The table `T` has size `N`. Element whose key is `k` is pointed by `T[k]`.
If there's no element for a key, it's marked `None`.

Dictionary algorithms:

    def search(T, k):
        return T[k]

    def insert(T, x):
        T[x.key] = x

    def delete(T, x):
        T[x.key] = None

The three algorithms are `O(1)` if the table is an array.
