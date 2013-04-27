#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Goldbach's other conjecture
Problem 46
http://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a base.

    9 = 7 + 2×1²
    15 = 7 + 2×2²
    21 = 3 + 2×3²
    25 = 7 + 2×3²
    27 = 19 + 2×2²
    33 = 31 + 2×1²

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a base?

"""


limit = 10000  # limit by guessing
smallest_odd_composite = None

primes = [True for n in xrange(0, limit + 1)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False

# a composite number is any positive integer greater than one that is not a
# prime number.
comp_num = (n for n in xrange(limit) if not primes[n] and n > 1 and n % 2 != 0)
for num in comp_num:
    for prime in (p for p in xrange(num) if primes[p]):
        base = ((num - prime) / 2) ** 0.5
        if int(base) == base:
            break
    else:
        smallest_odd_composite = num
        break

print smallest_odd_composite
