#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Prime digit replacements
Problem 51
http://projecteuler.net/problem=51

By replacing the 1ˢᵗ digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are prime_nums prime.

By replacing the 3ʳᵈ and 4ᵗʰ digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

"""


import sys
from collections import Counter
limit = 1950000

primes = [True for num in xrange(limit)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(2, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False

for num in (n for n in xrange(100, 150000) if primes[n]):
    b = Counter(str(num))
    for m in (k for k in b if b[k] >= 2):
        proposal = {int(str(num).replace(str(m), str(o))) for o in xrange(10)}
        filtered = {p for p in proposal if primes[p] if
                    len(str(p)) == len(str(num))}
        if len(filtered) == 8:
            print sorted(filtered)[0]
            sys.exit()
