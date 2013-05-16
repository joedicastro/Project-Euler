#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Path sum: two ways
Problem 81
http://projecteuler.net/problem=81

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red
and is equal to 2427.

131  673  234  103   18
201   96  342  965  150
630  803  746  422  111
537  699  497  121  956
805  732  524   37  331

Find the minimal path sum, in <matrix.txt> (right click and 'Save Link/Target
As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the
bottom right by only moving right and down.

"""


matrix_raw = open('matrix.txt', 'r').read().splitlines()
matrix = [[int(n) for n in l.split(',')] for l in matrix_raw if l]

# first, to generate the coordinates to traverse the matrix diagonally moving
# to the left and up, beginning at the bottom right and ending on the top left
diagonals = []

last_row = end = len(matrix) - 1

for diagonal in xrange(2 * end - 1, -1, -1):
    for number in xrange(diagonal - end, end + 1):
        diagonals.append((diagonal - number, number))
        if number == 0:
            end -= 1

# now, traverse the matrix adding the minimal sum from bottom right to top left
for row, col in diagonals:
    if row == last_row:
        matrix[row][col] = matrix[row][col] + matrix[row][col + 1]
    elif col == last_row:
        matrix[row][col] = matrix[row][col] + matrix[row + 1][col]
    else:
        matrix[row][col] = min(matrix[row][col] + matrix[row][col + 1],
                               matrix[row][col] + matrix[row + 1][col])

print 'The answer is {0}'.format(matrix[0][0])
