#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Consecutive prime sum
Problem 50
http://projecteuler.net/problem=50


The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


limit = 1000000

primes = [True for n in xrange(0, limit)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False

putl = [i for i in xrange(len(primes)) if primes[i]]

maximum, number = 2, 0
for n in putl:
    if n <= putl[-1] - number:
        up = maximum
        while putl[up] != putl[-1]:
            rango = putl[putl.index(n):up]
            summatory, lenght = sum(rango), len(rango)
            up += 1
            if summatory > putl[-1]:
                break
            elif summatory in putl and lenght > maximum:
                maximum, number, up = lenght, summatory, lenght

print 'The number is {0} as a sum of {1} consecutive primes'.format(number,
                                                                    maximum)
