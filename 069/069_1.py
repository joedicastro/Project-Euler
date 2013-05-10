#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Totient maximum
Problem 69
http://projecteuler.net/problem=69


Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

n   Relatively Prime    φ(n)    n/φ(n)
2   1                   1       2
3   1,2                 2       1.5
4   1,3                 2       2
5   1,2,3,4             4       1.25
6   1,5                 2       3
7   1,2,3,4,5,6         6       1.1666...
8   1,3,5,7             4       2
9   1,2,4,5,7,8         6       1.5
10  1,3,7,9             4       2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

"""

# after a previous analysis, I had this:
#
# maximum for n ≤     10 is     6
# maximum for n ≤    100 is    30
# maximum for n ≤   1000 is   210
# maximum for n ≤  10000 is  2310
# ...
#
# I saw a pattern there:
#
#      6
#     30 =    6 x  5
#    210 =   30 x  7
#   2310 =  210 x 11
#
# so, the solution is pretty simple...

print reduce(lambda x, y: x * y, [2, 3, 5, 7, 11, 13, 17])



#=============================================================================+
# Code used for the previous analysis, runs in ±42s
#=============================================================================+

# from fractions import gcd

# limit = 10000

# primes = [True for n in xrange(0, limit)]
# primes[0], primes[1] = False, False  # 0 and 1 are not primes

# for i in xrange(1, int(limit ** 0.5 + 1)):
#     if primes[i]:
#         for j in xrange(i ** 2, limit, i):
#             primes[j] = False


# maximum, maximums = 0, []

# for i in xrange(2, 10000):
#     if not primes[i]:
#         coprimes = sum(1 for j in xrange(1, i) if gcd(i, j) == 1)
#         ratio = i / float(coprimes)
#         if ratio > maximum:
#             maximums.append(i)
#             maximum = ratio

# print maximums
