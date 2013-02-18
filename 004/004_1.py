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
x = 999
while x >= 100:
    y = 999
    while y >= x:
        if x % 11 == 0 or y % 11 == 0:
            if x * y <= largest:
                break

            if is_palindrome(x * y):
                largest = x * y

        y -= 1
    x -= 1

print largest

###########################################################################
#                                 Answer                                  #
###########################################################################

#  906609
