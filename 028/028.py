#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Number spiral diagonals
Problem 28
http://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

"""

# REASONING:
#
# If we take only the right half of the diagonals:
#
#   9 + 25 + 3 + 13 = 50
#
# multiply the result by two and add the central number, 1:
#
#   (50 x 2) + 1 = 101
#
# The same occurs with 7x7, 9x9, 11x11 spirals and so on.
#
# So, we need only to find the right half of the spiral's diagonals.
# And if we take a closer look, we can see this:
#
# right-upper quadrant (9, 25):
#
#   for a 5x5 spiral: 3², 5²
#   for a 7x7 spiral: 3², 5², 7²
#   for a 9x9 spiral: 3², 5², 7², 9²
#   ...
#
# right-lower quadrant (3, 13):
#
#   for a 5x5 spiral: 3² - 6, 5² - 6 x 2
#   for a 7x7 spiral: 3² - 6, 5² - 6 x 2, 7² - 6 x 3
#   for a 9x9 spiral: 3² - 6, 5² - 6 x 2, 7² - 6 x 3, 9² - 6 x 4
#   ...
#

spiral_dimension = 1001

# right upper quadrant
ruq = [(x + 2) ** 2 for x in xrange(1, spiral_dimension, 2)]
# right lower quadrant
rlq = [ruq[i] - (6 * (i + 1)) for i in xrange(len(ruq))]

print (sum(ruq) + sum(rlq)) * 2 + 1
