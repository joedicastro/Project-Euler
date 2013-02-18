#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Truncatable primes
Problem 37
http://projecteuler.net/problem=37


The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


def is_truncatable(n, primes_lst):
    for i in xrange(1, len(str(n))):
        if not primes_lst[int(str(n)[i:])] or not primes_lst[int(str(n)[:i])]:
            return False
    return True


limit = 1000000

primes = [True for n in xrange(0, limit)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False

total = 0
for prime in xrange(1, len(primes)):
    if primes[prime]:
        if is_truncatable(prime, primes) and prime not in (2, 3, 5, 7):
            total += prime

print total

###########################################################################
#                                  Answer                                 #
###########################################################################

# 748317
