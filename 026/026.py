#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Reciprocal cycles
Problem 26
http://projecteuler.net/problem=26


A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the number of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""


longest = 0
number = 0

for denominator in range(1, 1000):
    numerator, remainder, remainders = 1, 1, []
    while remainder:
        while numerator < denominator:
            numerator *= 10
        remainder = numerator % denominator
        remainders.append(remainder)
        numerator = remainder
        if remainders.count(remainder) > 1:
            length_recurring_cycle = len(set(remainders))
            if length_recurring_cycle > longest:
                longest, number = length_recurring_cycle, denominator
            break


print 'The number is {0} with a period of {1} digits'.format(number, longest)
