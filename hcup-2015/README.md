# `10-homework.py`

The main algorithm here is coded in the `question()` function. This function receeives a range `r` and a number `k` and it has to return how many of the numbers in that range have a primacity of exactly `k`.

The idea here was to go through each element of the range, one by one, and calculating its primacity. If the primacity was `k`, then this number was kept, otherwise, it was discarded. Once we have the list of all the numbers whose primacity is `k`, we return the length of that list.

The primacity of an integer `i` is calculated by going throught each of the divisors of `i` and keeping in a list only those that are prime numbers; the length of that list is the primacity. Divisors of `i` are calculated by going through each integer between 1 and `i` and testing whether it divides `i`. The test for whether a number is prime basically checks if the number has exactly two divisors.

Complexity for this algorithm is:
