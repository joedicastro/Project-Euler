#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Powerful digit sum
Problem 56
http://projecteuler.net/problem=56


A googol (10¹⁰⁰) is a massive number: one followed by one-hundred zeros; 100¹⁰⁰
is almost unimaginably large: one followed by two-hundred zeros. Despite their
size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, aᵇ, where a, b < 100, what is the
maximum digital sum?
"""


maximum = 0
for i in xrange(1, 100):
    for j in xrange(1, 100):
        digital_sum = sum((int(i) for i in str(i ** j)))
        if digital_sum > maximum:
            maximum = digital_sum

print maximum

###########################################################################
#                                  Answer                                 #
###########################################################################

# 972
