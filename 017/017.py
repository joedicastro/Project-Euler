#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Number letter counts
Problem 17
http://projecteuler.net/problem=17


If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total_of_letters.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
           7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
           12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
           16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
           20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
           70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred',
           1000: 'thousand'}

total_of_letters = 0

for i in xrange(1, 1001):
    num_in_letters = ''
    thousands = i // 1000
    hundreds = (i % 1000) // 100
    tens = ((i % 1000) % 100) // 10
    ones = ((i % 1000) % 100) % 10
    if thousands:
        num_in_letters += numbers[thousands] + ' ' + numbers[1000] + ' '
    if hundreds:
        if not tens and not ones:
            num_in_letters += numbers[hundreds] + ' ' + numbers[100]
        else:
            num_in_letters += numbers[hundreds] + ' ' + numbers[100] + ' and '
    if tens:
        if tens > 1:
            if ones:
                num_in_letters += numbers[tens * 10] + '-'
            else:
                num_in_letters += numbers[tens * 10]
        else:
            num_in_letters += numbers[int('1' + str(ones))]
    if ones and tens != 1:
        num_in_letters += numbers[ones]

    total_of_letters += len(num_in_letters.replace(' ', '').replace('-', ''))

print total_of_letters

###########################################################################
#                                  Answer                                 #
###########################################################################

# 21124
