#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Large non-Mersenne prime
Problem 97
http://projecteuler.net/problem=97

The first known prime found to exceed one million digits was discovered in
1999, and is a Mersenne prime of the form 2⁶⁹⁷²⁵⁹³−1; it contains exactly
2,098,960 digits. Subsequently other Mersenne primes, of the form 2ᵖ−1, have
been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433×2⁷⁸³⁰⁴⁵⁷+1.

Find the last ten digits of this prime number.

"""

prime = (28433 * 2 ** 7830457) + 1

print divmod(prime, 10 ** 10)[1]
