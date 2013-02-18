#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Combinatoric selections
Problem 53
http://projecteuler.net/problem=53


There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ⁵C₃ = 10.

In general,

ⁿCᵣ = n! / r!(n - r)!, where r ≤ n, n! = n x (n - 1) x...x3 x 2 x 1, and 0! = 1

It is not until n = 23, that a value exceeds one-million: ²³C₁₀ = 1144066.

How many, not necessarily distinct, values of ⁿCᵣ, for 1 ≤ n ≤ 100, are
greater than one-million?
"""


from math import factorial

total = 0
for n in xrange(23, 101):
    for r in xrange(1, n - 1):
        if n >= r:
            if factorial(n) / (factorial(r) * factorial(n - r)) > 1000000:
                total += 1

print total

###########################################################################
#                                  Answer                                 #
###########################################################################

# 4075
