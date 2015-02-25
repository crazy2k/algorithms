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
* **Idea**: Table `T` has size `n`. `T[k]` points to element whose key is `k`,
  or is marked `None` if there's no such element in the dynamic set.
* Dictionary algorithms:

        def search(T, k):
            return T[k]

        def insert(T, x):
            T[x.key] = x

        def delete(T, x):
            T[x.key] = None

  * The three are `O(1)` if the table is an array.

# Hash tables

* **Idea**: Table `T` has size `m`. The element whose key is `k`, if it is in
  the dynamic set, can be found in `T[h(k)]`, where `h()` is a hashing
  function.
* Problem: Different elements can have the same hash value (collision).
  * Solution: Collision resolution by chaining. `T[h(k)]` is actually a
    (preferably, doubly-linked) list with all the elements with the same
    `h(k)`.
* Dictionary algorithms:

        def search(T, k):
            traverse list T[h(x.key)] looking for element whose key is k

        def insert(T, x):
            insert x in the list T[h(x.key)]

        def delete(T, x):
            delete x from the list T[h(x.key)]
 
  * Insert is `O(1)`. Delete can be `O(1)` if list is doubly-linked. Search is
    `O(n)` in the worst case but it can be `O(1)` in average if using simple
    uniform hashing (any element can fall into any slot with same probability)
