#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Cyclical figurate numbers
Problem 61
http://projecteuler.net/problem=61

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
all figurate (polygonal) numbers and are generated by the following formulae:

Triangle    P₃,ₙ=n(n+1)/2       1, 3, 6, 10, 15, ...
Square      P₄,ₙ=n²             1, 4, 9, 16, 25, ...
Pentagonal  P₅,ₙ=n(3n−1)/2      1, 5, 12, 22, 35, ...
Hexagonal   P₆,ₙ=n(2n−1)        1, 6, 15, 28, 45, ...
Heptagonal  P₇,ₙ=n(5n−3)/2      1, 7, 18, 34, 55, ...
Octagonal   P₈,ₙ=n(3n−2)        1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

1. The set is cyclic, in that the last two digits of each number is the first
two digits of the next number (including the last number with the first).

2. Each polygonal type: triangle (P₃_,₁₂₇=8128), square (P₄_,₉₁=8281), and
pentagonal (P₅_,₄₄=2882), is represented by a different number in the set.

3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal, is represented by a different number in the set.

"""


import sys


def get_options(num, array):
    return (i for i in array if str(num)[-2:] == str(i)[:2])


def is_cyclic(array):
    if array:
        suffixes = set(str(s)[-2:] for s in array)
        prefixes = set(str(p)[:2] for p in array)
        if len(suffixes) == len(array):
            if suffixes == prefixes:
                return True


def in_each_type(array, types):
    for i in types:
        if len(i.intersection(array)) != 1:
            return False
    return True


limit = 200

triangle = set((t * (t + 1)) / 2 for t in xrange(limit))
square = set(s ** 2 for s in xrange(limit))
pentagonal = set((p * (3 * p - 1)) / 2 for p in xrange(limit))
hexagonal = set(x * (2 * x - 1) for x in xrange(limit))
heptagonal = set((h * (5 * h - 3)) / 2 for h in xrange(limit))
octagonal = set((o * (3 * o - 2)) for o in xrange(limit))

# we only need 4-digit numbers, and heptagonal is a subset of triangle, so:
all_types = set(n for n in set.union(triangle, square, pentagonal, heptagonal,
                                     octagonal) if len(str(n)) == 4)

# if a number is in hexagonal is also in triangle, so:
types = (square, pentagonal, hexagonal, heptagonal, octagonal)

for first in sorted(all_types):
    for second in get_options(first, all_types):
        for third in get_options(second, all_types):
            for fourth in get_options(third, all_types):
                for fifth in get_options(fourth, all_types):
                    for sixth in get_options(fifth, all_types):
                        numbers = [first, second, third, fourth, fifth, sixth]
                        if is_cyclic(numbers) and in_each_type(numbers, types):
                            print 'The sum is {0}'.format(sum(numbers))
                            sys.exit()
