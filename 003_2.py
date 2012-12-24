#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


import math


def is_prime(number):
    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True

number = 600851475143
i = 2

while i < number:
    if is_prime(i):
        while number % i == 0:
            number = number / i
    i += 1

print i



###########################################################################
#                                 Answer                                  #
###########################################################################

# 6857
