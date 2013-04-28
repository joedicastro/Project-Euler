#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Distinct primes factors
Problem 47
http://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?

"""

limit = 150000  # limit by guessing

primes = [True for n in xrange(0, limit + 1)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False

num_consecutive_numbers_et_prime_factors = 4
consecutive = set()

for number in (a for a in xrange(646, limit) if not primes[a]):
    count = set()
    num = number
    factors = (n for n in xrange(num + 1) if primes[n])
    factor = factors.next()
    while num != 1:
        if num % factor == 0:
            num = num / factor
            count.add(factor)
        else:
            factor = factors.next()
    if len(count) == num_consecutive_numbers_et_prime_factors:
        if (number - 1) in consecutive:
            consecutive.add(number)
            if len(consecutive) == num_consecutive_numbers_et_prime_factors:
                print consecutive.pop()
                break
        else:
            consecutive.clear()
            consecutive.add(number)
