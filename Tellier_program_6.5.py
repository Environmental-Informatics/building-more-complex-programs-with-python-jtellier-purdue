#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:34:55 2020

@author: jtellier
"""

"""function for finding the greatest common divisor
between twointegers a and b. In this function, a must
be greater than b. """
def gcd(a, b):
    if b == 0: #if b equals zero, the GCD is a
        return a
    else:
        return gcd(b, a % b) #otherwise we use the modulus to compute the
        #remainder and recursively call the function
gcd(15, 10) #testing the function
