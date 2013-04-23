#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Maximum path sum II
Problem 67
http://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

     3
    7 4
   2 4 6
  8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in <triangle.txt> (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem, as there are 2⁹⁹
altogether! If you could check one trillion (10¹²) routes every second it would
take over twenty billion years to check them all. There is an efficient
algorithm to solve it. ;o)


"""

triangle_raw = open('triangle.txt', 'r').read()

triangle = [[int(n) for n in l.split()] for l in triangle_raw.split('\n') if l]

for row in xrange(len(triangle) - 1, -1, -1):
    for number in xrange(len(triangle[row]) - 1):
        chosen = max(triangle[row][number] + triangle[row - 1][number],
                     triangle[row][number + 1] + triangle[row - 1][number])
        triangle[row - 1][number] = chosen

print 'The answer is {0}'.format(triangle[0][0])
