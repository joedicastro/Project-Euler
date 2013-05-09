#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Square root convergents
Problem 57
http://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?

"""

# I you pay attenttion, you can see this:
#
# 3/2 → 7/5 ≈ 3 x (1 + √2) / 2 x (1 + √2)
# 7/5 → 17/12 ≈ 7 x (1 + √2) / 5 x (1 + √2)
# 17/12 → 41/29 ≈ 17 x (1 + √2) / 12 x (1 + √2)
# ...
#
# so, to be more precise:
#
# 3/2 → 7/5 = 7.424 / 4.828
# and after round both numbers to an integer becomes = 7/5

from decimal import Decimal, getcontext
from math import sqrt

# the numbers grow too fast, so let's use decimal and a big precission in order
# to solve the problem by brute force.
getcontext().prec = 400

total = 0
numerator, denominator = 3, 2

def calculate(next_number):
    next_number = (next_number * Decimal(1 + sqrt(2)))
    # due to the big numbers and some problems rounding, round them by hand
    next_number += 1 if ((next_number * 10 % 10) * 2) > 5 else 0
    # finally, return to a long integer
    return long(next_number)


for i in xrange(1000):
    numerator, denominator = calculate(numerator), calculate(denominator)
    if len(str(numerator)) > len(str(denominator)):
        total += 1

print total
