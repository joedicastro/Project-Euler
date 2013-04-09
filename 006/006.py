#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Sum square difference
Problem 6
http://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

numbers_up_to = 100

sum_of_squares = sum(x ** 2 for x in xrange(1, numbers_up_to + 1))
square_of_sum = sum(y for y in xrange(1, numbers_up_to + 1)) ** 2

print  square_of_sum - sum_of_squares
