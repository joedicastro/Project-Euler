#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Digit factorials
Problem 34
http://projecteuler.net/problem=34


145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

# 0! = 1
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5040
# 8! = 40320
# 9! = 362880
#
# So, we have
#
# 9! * 8 = 2903040 a 7 digits number
# 9! * 7 = 2540160 a 7 digits number so 2540160 is our upper limit


def sum_fact_digits(n):
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    if n / 10 < 1:
        return factorials[n]
    else:
        return factorials[n % 10] + sum_fact_digits(n / 10)

total = 0
for i in xrange(10, 2540160):
    if i == sum_fact_digits(i):
        total += i

print total

###########################################################################
#                                  Answer                                 #
###########################################################################

# 40730
