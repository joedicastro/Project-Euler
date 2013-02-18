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


def collatz_sequence(i):
    yield i
    while i > 1:
        i = i / 2 if i % 2 == 0 else 3 * i + 1
        yield i

longest_chain = []

for i in xrange(1000000, 1, -1):
    sequence = list(collatz_sequence(i))
    if len(sequence) > len(longest_chain):
        longest_chain = sequence

print longest_chain[0]

###########################################################################
#                                  Answer                                 #
###########################################################################

# 837799
