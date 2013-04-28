#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Distinct primes numbers
Problem 47
http://projecteuler.net/problem=47

The first two consecutive nums to have two distinct prime numbers are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive nums to have three distinct prime numbers are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime numbers.
What is the first of these nums?

"""


limit = 150000  # limit by guessing
numbers = [0 for num in xrange(limit)]

for num in xrange(2, limit):
    if numbers[num] == 0:
        for j in xrange(num, limit, num):
            numbers[j] += 1
    elif numbers[num] == 4 and len(set(numbers[num - 3:num + 1])) == 1:
        print num - 3
        break
