#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Longest Collatz sequence
Problem 14
http://projecteuler.net/problem=14



The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""


longest, start = 1, 1
previous = {}

for i in xrange(1, 1000000):
    count = 1
    j = i
    while j > 1:
        if j in previous:
            count += previous[j]
            break
        j = j / 2 if j % 2 == 0 else 3 * j + 1
        count += 1
    if count > longest:
        longest, start = count, i
    previous[i] = count

print start
