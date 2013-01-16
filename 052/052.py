#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Permuted multiples
Problem 52
http://projecteuler.net/problem=52


It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

# assuming 125874 as the lower limit
for i in xrange(125874, 1000000):
    if len(set(''.join(sorted(str(i * x))) for x in xrange(2, 7))) == 1:
        print i
        break

###########################################################################
#                                  Answer                                 #
###########################################################################

# 142857
