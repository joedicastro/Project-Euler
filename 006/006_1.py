#!/usr/bin/env python
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
nut_plus_one = numbers_up_to + 1

sum_of_squares = ((numbers_up_to * nut_plus_one) / 2) ** 2
square_of_sum = ((2 * numbers_up_to + 1) * nut_plus_one * numbers_up_to) / 6

print  sum_of_squares - square_of_sum

###########################################################################
#                                 Answer                                  #
###########################################################################

# 25164150
