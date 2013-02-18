#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Multiples of 3 and 5
Problem 1
http://projecteuler.net/problem=1

 If we list all the natural numbers below 10 that are multiples of 3 or 5, we
 get 3, 5, 6 and 9. The sum of these multiples is 23.

 Find the sum of all the multiples of 3 or 5 below 1000.
"""

by_3 = (i for i in xrange(1, 1000) if i % 3 == 0)
by_5 = (i for i in xrange(1, 1000) if i % 5 == 0)
by_15 = (i for i in xrange(1, 1000) if i % 15 == 0)

print sum(by_3) + sum(by_5) - sum(by_15)


###########################################################################
#                                 Answer                                  #
###########################################################################

# 233168
