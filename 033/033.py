#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Digit canceling fractions
Problem 33
http://projecteuler.net/problem=33

The fraction ⁴⁹/₉₈ is numerator curious fraction, as an inexperienced
mathematician in attempting to cancel_digit it may incorrectly believe that
⁴⁹/₉₈ = ⁴/₈, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, ³⁰/₅₀ = ³/₅, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

"""


# Euclidian algorithm
def great_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def cancel_digit(x, y):
    xx = ''.join(d for d in str(x) if d not in str(y))
    yy = ''.join(d for d in str(y) if d not in str(x))
    if len(xx) == 1 and len(yy) == 1 and yy != '0':
        return float(xx) / float(yy)


numerators, denominators = [], []
simplified_numerators, simplified_denominators = [], []

for numerator in xrange(10, 100):
    for denominator in xrange(10, 100):
        # let's avoid the trivial examples, multiples of ten
        if numerator < denominator and (denominator % 10 != 0):
            simplified = cancel_digit(numerator, denominator)
            if simplified:
                if float(numerator) / float(denominator) == simplified:
                    numerators.append(numerator)
                    denominators.append(denominator)


print "The four non-trivial examples are:\n"
for num, den in zip(numerators, denominators):
    print '{0}/{1}'.format(num, den)
    gcd = great_common_divisor(num, den)
    simplified_numerators.append(num / gcd)
    simplified_denominators.append(den / gcd)

print "\nThe simplified fractions are:\n"
for snum, sden in zip(simplified_numerators, simplified_denominators):
    print '{0}/{1}'.format(snum, sden)

product = [reduce(lambda x, y: x * y, simplified_numerators),
           reduce(lambda x, y: x * y, simplified_denominators)]

gcd_product = great_common_divisor(*product)

print """
The product is:

{0}/{1}

and the denominator is:

{1}
""".format(product[0] / gcd_product, product[1] / gcd_product)
