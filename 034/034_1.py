#!/usr/bin/env python2
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


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

factorials = [factorial(n) for n in xrange(10)]

total = 0
cache = [1, 1, 2]
for i in xrange(3, 10000):
    subtotal = sum(factorials[int(d)] for d in str(i))
    cache.append(subtotal)
    if i == subtotal:
        total += i

for i in xrange(10000, 2540160):
    left, right = i // 10000, i % 10000
    zeros = (len(str(i)) - len('{0}{1}'.format(left, right)))
    if i == cache[left] + cache[right] + zeros:
        total += i

print total
