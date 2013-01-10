#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Summation of primes
Problem 10
http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import math


def is_prime(number):
    for n in xrange(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True


i = 1
# let's assume 2 and 3 as prime numbers by default
sum = 5

while 6 * i + 1 < 2000000:
    for x in (6 * i - 1, 6 * i + 1):
        if is_prime(x):
            sum += x
    i += 1

print sum

###########################################################################
#                                 Answer                                  #
###########################################################################

# 142913828922
