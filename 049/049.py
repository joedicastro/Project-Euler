#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Prime permutations
Problem 49
http://projecteuler.net/problem=49


The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""


from itertools import permutations
from sys import exit


limit = 10000

primes = [True for n in xrange(0, limit)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit ** 0.5)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False


for i in xrange(1000, 10000):
    if primes[i] and '0' not in str(i):
        all_permutations = set(int(''.join(i)) for i in permutations(str(i)))
        only_primes = [i for i in sorted(all_permutations) if primes[i]]
        while len(only_primes) >= 3:
            if sum(only_primes[0:3]) / 3 == only_primes[1]:
                print ''.join(str(n) for n in only_primes[0:3])
                exit()
            else:
                only_primes.pop(0)

###########################################################################
#                                  Answer                                 #
###########################################################################

# 296962999629
