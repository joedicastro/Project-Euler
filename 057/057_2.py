#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Square root convergents
Problem 57
http://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?

"""

# I you pay attenttion, you can see this:
#
# 3/2 → 7/5 = (2 x 2) + 3 / 3 + 2
# 7/5 → 17/12 = (2 x 5) + 7 / 7 + 5
# 17/12 → 41/29 = (2 x 12) + 17 / 17 + 12
# ...
#
# so, to be more precise:
#
# num / den → (2 x den) + num / num  + den


from math import log10

total = 0
nume, deno = 3, 2

for i in xrange(1000):
    if int(log10(nume)) > int(log10(deno)):
        total += 1
    nume, deno = (2 * deno) + nume, nume + deno

print total
