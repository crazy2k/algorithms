# Dynamic set

* The computational idea of a mathematical set.
* Can change over time: Its elements can be changed, and elements can be added
  or deleted from it, so the size of the set can change too.
* Usually, every element in the dynamic set has an associated identifying key.

## Dictionary operations

* **Search**: Given a dynamic set `S` and a key `k`, retrieve the element
  whose key is `k`.
* **Insert**: Given a dynamic set `S` and an element `x`, insert the element
  `x` in the dynamic set `S`.
* **Delete**: Given a dynamic set `S` and an element `x`, remove the element
  `x` from the dynamic set `S`.

# Direct-address tables

* Simple way to implement a dynamic set
* **Idea**: Table `T` has size `N`. `T[k]` points to element whose key is `k`,
  or is marked `None` if there's no such element in the dynamic set.
* Dictionary algorithms:

        def search(T, k):
            return T[k]

        def insert(T, x):
            T[x.key] = x

        def delete(T, x):
            T[x.key] = None

* The three are `O(1)` if the table is an array.
