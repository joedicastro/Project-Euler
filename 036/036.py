#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Double-base palindromes
Problem 36
http://projecteuler.net/problem=36


The decimal number, 585 = 1001001001₂ (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True

sum = 0

for i in xrange(1, 1000000):
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
        sum += i

print sum

###########################################################################
#                                  Answer                                 #
###########################################################################

# 872187
