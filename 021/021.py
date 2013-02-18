#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Amicable numbers
Problem 21
http://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).  If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def sum_divisors(num):
    i = 2
    limit = num ** 0.5
    total = 1
    while i < limit:
        if num % i == 0:
            if limit == int(limit):
                total += i
            else:
                total += i + num / i
        i += 1
    return total

amicable_numbers = []

for i in xrange(1, 10000):
    if i not in amicable_numbers:
        possible = sum_divisors(i)
        if possible > i:
            if sum_divisors(possible) == i:
                amicable_numbers += [i, possible]

print sum(amicable_numbers)

###########################################################################
#                                  Answer                                 #
###########################################################################

# 31626
