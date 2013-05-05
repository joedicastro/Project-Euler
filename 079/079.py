#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Passcode derivation
Problem 79
http://projecteuler.net/problem=79

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file, <keylog.txt>, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.

"""

from collections import defaultdict

attempts = open('keylog.txt').read().splitlines()

numbers = defaultdict(set)

# add for each digit, the digits that goes after it
for attempt in attempts:
    for number in xrange(3):
        numbers[int(attempt[number])] |= set([d for d in attempt[:number]])

# build the passcode by ordering its digits by the number of digits that goes
# after each one
passcode = ['0'] * len(numbers)
for d in numbers:
    passcode[len(numbers[d])] = str(d)

print ''.join(passcode)
