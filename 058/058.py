#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Spiral primes
Problem 58
http://projecteuler.net/problem=58

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

"""

import os


if os.path.exists('primes.txt'):
    cache = True
    primes = set()
    for line in open('primes.txt', 'r'):
        primes.add(int(line.rstrip()))
else:
    cache = False
    limit = 700000000

    primes = [True for n in xrange(0, limit)]
    primes[0], primes[1] = False, False  # 0 and 1 are not primes

    for i in xrange(1, int(limit ** 0.5 + 1)):
        if primes[i]:
            for j in xrange(i ** 2, limit, i):
                primes[j] = False

    with open('primes.txt', 'w') as output:
        for p in xrange(len(primes)):
            if primes[p]:
                output.write(str(p) + '\n')

all_nums, primes_in_diagonals = 1, 0
for layer in xrange(1, 13500):
    all_nums += 4.0
    nums = [((2 * layer + 1) ** 2) - n * layer for n in xrange(0, 8, 2)]
    if cache:
        primes_in_diagonals += len(primes.intersection(nums))
    else:
        primes_in_diagonals += sum(1 for n in nums if primes[n])
    if (primes_in_diagonals / all_nums) < 0.1:
        print 2 * layer + 1
        break
