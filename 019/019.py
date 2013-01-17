#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Counting Sundays
Problem 19
http://projecteuler.net/problem=19


You are given the following information, but you may prefer to do some research
for yourself.

  ∙ 1 Jan 1900 was a Monday.
  ∙ Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  ∙ A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?
"""

# 1 Jan 1900 was a Monday, a normal year are 365 days, and a week 7 days.
# 365 / 7 = 52,14 weeks, so 53 x 7 = 371 days, then 1 Jan 1901 was a Tuesday
# and 6 January the first Sunday of the twentieth century

days_for_year_from_1901_to_2000 = [0]

for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        if month in (4, 6, 9, 11):
            days_for_year_from_1901_to_2000 += xrange(1, 31)
        elif month == 2:
            # 2000 is the only century in this period divisible by 400
            if year % 4 == 0 or year == 2000:
                days_for_year_from_1901_to_2000 += xrange(1, 30)
            else:
                days_for_year_from_1901_to_2000 += xrange(1, 29)
        else:
            days_for_year_from_1901_to_2000 += xrange(1, 32)

total = 0
for sunday in xrange(6, len(days_for_year_from_1901_to_2000), 7):
    if days_for_year_from_1901_to_2000[sunday] == 1:
        total += 1

print total

###########################################################################
#                                  Answer                                 #
###########################################################################

# 171
