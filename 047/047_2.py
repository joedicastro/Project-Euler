#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Distinct primes factors
Problem 47
http://projecteuler.net/problem=47

The first two consecutive nums to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive nums to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these nums?

"""

limit_primes = 1000  # limit by guessing

primes = [True for n in xrange(0, limit_primes + 1)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit_primes ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit_primes, i):
            primes[j] = False

# num consecutive nums et prime factors
cons = 4
limit = 150000
nums = limit * [0]

for num in (a for a in xrange(14, limit)):
    count = set()
    for factor in (l for l in xrange(limit_primes) if primes[l]):
        if num % factor == 0:
            count.add(factor)
    nums[num] = len(count)
    if nums[num] == cons and len(set(nums[num - (cons - 1):num + 1])) == 1:
        print num - (cons - 1)
        break
