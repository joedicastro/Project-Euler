#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Largest exponential
Problem 99
http://projecteuler.net/problem=99


Comparing two numbers written in index form like 2¹¹ and 3⁷ is not difficult,
as any calculator would confirm that 2¹¹ = 2048 < 3⁷ = 2187.

However, confirming that 632382⁵¹⁸⁰⁶¹> 519432⁵²⁵⁸⁰⁶ would be much more
difficult, as both numbers contain over three million digits.

Using <base_exp.txt> (right click and 'Save Link/Target As...'), a 22K text
file containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.

"""

# as baseᵉˣᵖᵒⁿᵉⁿᵗ = eᵉˣᵖᵒⁿᵉⁿᵗ ˣ ˡⁿ⁽ᵇᵃˢᵉ⁾ , then in order to compare two powers,
# a bigger value of exponent x ln(base) means a bigger power


from math import log


lines = open('base_exp.txt').read().splitlines()

line, max_power = 0, 0

for i, power in enumerate(lines):
    base, exponent = power.split(',')
    exponent_of_e = int(exponent) * log(float(base))
    if exponent_of_e > max_power:
        line, max_power = i + 1, exponent_of_e

print line
