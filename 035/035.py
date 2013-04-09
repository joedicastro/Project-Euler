#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Circular primes
Problem 35
http://projecteuler.net/problem=35


The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""


def rotations(number):
    number_as_list = [i for i in str(number)]
    all_rots = [number]
    for i in xrange(1, len(number_as_list)):
        all_rots.append(int(''.join(number_as_list[i:] + number_as_list[:i])))
    return all_rots

limit = 1000000

primes = [True for n in xrange(0, limit)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False

circular_primes = []

for x in xrange(0, len(primes)):
    if all([primes[i] for i in rotations(x)]):
        circular_primes.append(x)

print len(circular_primes)
