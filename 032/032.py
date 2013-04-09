#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Pandigital products
Problem 32
http://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

# 987 x 98 = 96726 a total of ten digits, so there are no reason to search more
# far than 9876, the biggest 4-digit number possible to form part of the
# 1→9-pandigital multiplicand/multiplier/product identity
numbers_to_check = [i for i in xrange(1, 9877) if '0' not in str(i)]
products = []

for i in numbers_to_check:
    for j in numbers_to_check:
        if not i % j:
            if len(set('{0}{1}{2}'.format(i, j, (i / j)))) == 9:
                if i not in products and (i / j) in numbers_to_check:
                    products.append(i)

print sum(products)
