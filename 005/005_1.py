#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Smallest multiple
Problem 5
http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


# Euclidian algorithm
def great_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    return a * b / great_common_divisor(a, b)


def least_common_multiple_range(lst):
    return reduce(least_common_multiple, lst)


print least_common_multiple_range(range(1, 20))
