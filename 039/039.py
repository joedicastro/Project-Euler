#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Integer right triangles
Problem 39
http://projecteuler.net/problem=39


If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the perimeter of solutions maximised?
"""


solutions = {i: [] for i in xrange(1, 1001)}

for a in xrange(1, 1001):
    for b in xrange(1, 1001):
        c = (a ** 2 + b ** 2) ** 0.5
        if c == int(c):
            if a + b + c <= 1000:
                c = int(c)
                if sorted([a, b, c]) not in solutions[a + b + c]:
                    solutions[a + b + c].append(sorted([a, b, c]))

maximun, perimeter = 0, 0
for solution in solutions:
    if len(solutions[solution]) > maximun:
        maximun, perimeter = len(solutions[solution]), solution

print 'The perimeter is {0} with {1} solutions.'.format(perimeter, maximun)

###########################################################################
#                                  Answer                                 #
###########################################################################

# 840
