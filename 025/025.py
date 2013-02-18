#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
1000-digit Fibonacci number
Problem 25
http://projecteuler.net/problem=25


The Fibonacci sequence is defined by the recurrence relation:

    Fₙ = Fₙ₋₁ + Fₙ₋₂, where F₁ = 1 and F₂ = 1.

Hence the first 12 terms will be:

    F₁ = 1
    F₂ = 1
    F₃ = 2
    F₄ = 3
    F₅ = 5
    F₆ = 8
    F₇ = 13
    F₈ = 21
    F₉ = 34
    F₁₀ = 55
    F₁₁ = 89
    F₁₂ = 144

The 12th term, F₁₂, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

"""


fibonacci = [1, 1]

while len(str(fibonacci[-1])) < 1000:
    next = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next)

print len(fibonacci)

###########################################################################
#                                  Answer                                 #
###########################################################################

# 4782
