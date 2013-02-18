#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Self powers
Problem 48
http://projecteuler.net/problem=48


The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.

Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
"""

sum = 0

for x in xrange(1, 1001):
    sum += x ** x

print str(sum)[-10:]

###########################################################################
#                                  Answer                                 #
###########################################################################

# 9110846700
