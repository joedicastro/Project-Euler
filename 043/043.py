#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Sub-string divisibility
Problem 43
http://projecteuler.net/problem=43


The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d₁ be the 1ˢᵗ digit, d₂ be the 2ⁿᵈ digit, and so on. In this way, we note
the following:

    d₂d₃d₄=406 is divisible by 2
    d₃d₄d₅=063 is divisible by 3
    d₄d₅d₆=635 is divisible by 5
    d₅d₆d₇=357 is divisible by 7
    d₆d₇d₈=572 is divisible by 11
    d₇d₈d₉=728 is divisible by 13
    d₈d₉d₁₀=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


import itertools

sum = 0

for i in itertools.permutations(xrange(0, 10)):
    if i[0] != 0:
        number = ''.join(str(j) for j in i)
        property = True
        for j, k in zip(xrange(1, 8), (2, 3, 5, 7, 11, 13, 17)):
            if int(number[j:j + 3]) % k != 0:
                property = False
                break
        if property:
            sum += int(number)

print sum
