#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Square digit chains
Problem 92
http://projecteuler.net/problem=92


A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""


count = 0
cache = set()
for n in xrange(2, 100):
    r = ''.join(j for j in sorted(str(n)))
    if r in cache:
        count += 1
    else:
        while n != 89 or n != 1:
            if n in cache:
                count += 1
                break
            elif n == 89:
                count += 1
                cache.add(r)
                break
            elif n == 1:
                break
            else:
                n = sum(int(i) ** 2 for i in str(n))


print len(cache)
print count

###########################################################################
#                                  Answer                                 #
###########################################################################

# 8581146
