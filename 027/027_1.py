#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Quadratic primes
Problem 27
http://projecteuler.net/problem=27

Euler published the remarkable quadratic formula:

    n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² − 79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n

    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.

"""

# Let's calculate the maximum prime number possible:
#
# 1000² + 1000 x 1000 + 1000 = 2 x 1000² + 1000 = 2001000
#
# That's not a prime, so adjust to the closer prime: 2000989

limit = 2000989

primes = [True for n in xrange(0, limit + 1)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in xrange(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, limit, i):
            primes[j] = False

maximum, product, coeff_a, coeff_b = None, None, None, None

# for n = 0, b needs to be prime and primes are only positive numbers
# the only odd prime number is 2, then a must be odd too
for a in xrange(-1000, 1000):
    if a % 2 != 0:
        for b in range(2, 1000):
            for n in xrange(0, abs(a) + 1):
                if primes[b]:
                    result = (n ** 2) + (a * n) + b
                    if not primes[result]:
                        break
                else:
                    break
            else:
                if n > maximum:
                    maximum, product = n, a * b
                    coeff_a, coeff_b = a, b

print """The product is {0} for a maximum of {1} consecutive primes when
 = {2} and b = {3}""".format(product, maximum + 1, coeff_a, coeff_b)
