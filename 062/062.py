#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Cubic permutations
Problem 62
http://projecteuler.net/problem=62

The cube, 41063625 (345³), can be permuted to produce two other cubes: 56623104
(384³) and 66430125 (405³). In fact, 41063625 is the smallest cube which has
exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.

"""

from collections import Counter

limit = 10000

cubes = [num ** 3 for num in xrange(2, limit)]

for tens in (10 ** x for x in xrange(1, 15)):
    cubes_in_range = [cube for cube in cubes if (tens / 10) < cube < tens]
    strings = [''.join(sorted(str(n))) for n in cubes_in_range]
    count = Counter(strings)
    if 5 in count.values():
        match = [key for key in count.keys() if count[key] == 5]
        print min(b for a, b in zip(strings, cubes_in_range) if a in match)
        break
