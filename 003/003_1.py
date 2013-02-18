#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Largest prime factor
Problem 3
http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


number = 600851475143
i = 2

while i < number:
    while number % i == 0:
        number = number / i
    i += 1 if (i + 1) % 2 != 0 else 2  # skip pairs

print i


###########################################################################
#                                 Answer                                  #
###########################################################################

# 6857
