#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
10001st prime
Problem 7
http://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""


import math


def is_prime(number):
    for n in xrange(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True


i = 1
# let's assume 2 and 3 as prime numbers by default
prime_numbers = [2, 3]

while len(prime_numbers) < 10001:
    for x in (6 * i - 1, 6 * i + 1):
        if is_prime(x):
            prime_numbers.append(x)
    i += 1

print max(prime_numbers)
