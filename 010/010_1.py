#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Summation of primes
Problem 10
http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


limit = 2000000

primes = [True for n in xrange(0, limit)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False

sum = 0

for x in xrange(0, len(primes)):
    if primes[x]:
        sum += x

print sum

###########################################################################
#                                 Answer                                  #
###########################################################################

# 142913828922
