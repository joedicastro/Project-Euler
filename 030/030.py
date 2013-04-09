#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Digit fifth powers
Problem 30
http://projecteuler.net/problem=30


Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
    8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
    9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴

As 1 = 1⁴ is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

# We have that,
#
# 9⁵ x 4 = 236196
# 9⁵ x 5 = 295245
# 9⁵ x 6 = 354294
# 9⁵ x 7 = 413343
# 9⁵ X 6 is not enough to make a 7 digits number, so 354294 will be out limit

numbers = set()

for i in xrange(2, 354294):
    if sum([int(j) ** 5 for j in str(i)]) == i:
        numbers.add(i)

print sum(numbers)
