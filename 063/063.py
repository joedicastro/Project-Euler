#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Powerful digit counts
Problem 63
http://projecteuler.net/problem=63


The 5-digit number, 16807=7⁵, is also a fifth power. Similarly, the 9-digit
number, 134217728=8⁹, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

# if the base is 10 or more the power will always have more digits than the
# exponent.

total = 0

for base in xrange(1, 10):
    for exponent in xrange(1, 100):
        if len(str(base ** exponent)) == exponent:
            total += 1

print total
