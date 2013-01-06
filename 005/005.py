#!/usr/bin/env python
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


def evenly_divisible_by(number, from_1_to):
    for num in range(from_1_to - 1, 1, -1):
        if number % num != 0:
            return False
    return True

numbers_up_to = 20
smallest = numbers_up_to

while not evenly_divisible_by(smallest, numbers_up_to):
    smallest += numbers_up_to

print smallest

###########################################################################
#                                 Answer                                  #
###########################################################################

# 232792560
