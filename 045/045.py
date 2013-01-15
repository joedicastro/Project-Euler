#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Triangular, pentagonal, and hexagonal
Problem 45
http://projecteuler.net/problem=45



Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle 	  	Tₙ=n(n+1)/2     1, 3, 6, 10, 15, ...
Pentagonal 	  	Pₙ=n(3n-1)/2    1, 5, 12, 22, 35, ...
Hexagonal 	  	Hₙ=n(2n-1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T₂₈₅ = P₁₆₅ = H₁₄₃ = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

limit = 56000

triangle = {i * (i + 1) / 2 for i in xrange(2, limit)}
pentagonal = {i * (3 * i - 1) / 2 for i in xrange(2, limit)}
hexagonal = {i * (2 * i - 1) for i in xrange(2, limit)}

print list(pentagonal.intersection(hexagonal, triangle))[1]

###########################################################################
#                                  Answer                                 #
###########################################################################

# 1533776805
