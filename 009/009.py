#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Special Pythagorean triplet
Problem 9
http://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


# Using Euclid's formula. For m  = 23 and n = 22 we have (43, 924, 925), so we
# do not need to go long farther than that.
for n in xrange(1, 23):
    for m in xrange(n + 1, 24):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2

        if a + b + c == 1000:
            print '{0} * {1} * {2} = {3}'.format(a, b, c, a * b * c)
            break

###########################################################################
#                                 Answer                                  #
###########################################################################

# 31875000
