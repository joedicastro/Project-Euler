#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Pandigital prime
Problem 41
http://projecteuler.net/problem=41


We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import math
import itertools
import sys


def is_prime(number):
    for n in xrange(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True


digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1']

while digits:
    for j in sorted(list(itertools.permutations(digits)), reverse=True):
        number = int(''.join(j))
        if is_prime(number):
            print number
            sys.exit()
    digits.pop(0)

###########################################################################
#                                  Answer                                 #
###########################################################################

# 7652413
