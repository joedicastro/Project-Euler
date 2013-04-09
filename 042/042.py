#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Coded triangle numbers
Problem 42
http://projecteuler.net/problem=42


The nᵗʰ term of the sequence of triangle numbers is given by, tₙ = ½n(n+1);
so the first ten triangle numbers are:

            1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t₁₀. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""


import string

triangle_numbers = {i * (i + 1) / 2 for i in xrange(1, 20)}

letters = string.ascii_uppercase

words = sorted(open('words.txt', 'rb').read().replace('"', '').split(','))

print sum(1 for word in words if
          sum(letters.index(char) + 1 for char in word) in triangle_numbers)
