#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Largest palindrome product
Problem 4
http://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True

largest = 0

for x in xrange(999, 99, -1):
    for y in xrange(x, 99, -1):
        if is_palindrome(x * y):
            if x * y > largest:
                largest = x * y

print largest

###########################################################################
#                                 Answer                                  #
###########################################################################

#  906609
