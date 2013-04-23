#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Lattice paths
Problem 15
http://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

    p_015.gif

How many such routes are there through a 20×20 grid?

"""

# Using the formula for the central binomial coefficients

from math import factorial

grid_length = 20

print factorial(2 * grid_length) / (factorial(grid_length) ** 2)
