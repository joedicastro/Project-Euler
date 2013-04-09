#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Non-abundant sums
Problem 23
http://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

from math import sqrt


def sum_divisors(num):
    limit = sqrt(num)
    total = 1
    for i in xrange(2, int(limit) + 1):
        if num % i == 0:
            if i == limit:
                total += i
            else:
                total += i + num / i
    return total


limit = 28123
abundant_numbers = set()
sum_of_non_abundant = 0

for j in xrange(1, limit):
    if sum_divisors(j) > j:
        abundant_numbers.add(j)
    condition = True
    for x in abundant_numbers:
        if (j - x) in abundant_numbers:
            condition = False
            break
    if condition:
        sum_of_non_abundant += j

print sum_of_non_abundant
