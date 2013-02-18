#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Champernowne's constant
Problem 40
http://projecteuler.net/problem=40


An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12ᵗʰ digit of the fractional part is 1.

If dₙ represents the nᵗʰ digit of the fractional part, find the value of the
following expression.

    d₁ × d₁₀ × d₁₀₀ × d₁₀₀₀ × d₁₀₀₀₀ × d₁₀₀₀₀₀ × d₁₀₀₀₀₀₀
"""

champernowne = ''.join((str(i) for i in xrange(0, 1000001)))

print reduce(lambda x, y: x * y,
             [int(champernowne[10 ** i]) for i in xrange(0, 7)])

###########################################################################
#                                  Answer                                 #
###########################################################################

# 210
