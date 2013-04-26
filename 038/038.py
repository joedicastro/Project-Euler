#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Pandigital multiples
Problem 38
http://projecteuler.net/problem=38

Take the pandigital 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit pandigital that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

# 9999 X 1 = 9999
# 9999 x 2 = 19998
#
# If we use a digit more, the product never could be a 1 to 9 pandigital
# 9-digit pandigital, so no need to go more far than 9999

pandigital = 0
steps, number = 0, 0  # aux variables for a pretty result presentation

for integer in xrange(1, 10000):
    chain = ''
    for n in xrange(1, 10):
        if len(chain) == 9 and '0' not in chain and len(set(chain)) == 9:
            if int(chain) > pandigital:
                pandigital = int(chain)
                number, steps = integer, n
            break
        else:
            chain += str(integer * n)

print "The concatenated product is {0}\n".format(pandigital)
for j in xrange(1, steps):
    print '{0} x {1} = {2}'.format(number, j, number * j)
