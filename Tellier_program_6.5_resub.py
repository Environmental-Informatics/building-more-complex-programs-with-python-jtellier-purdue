#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:34:55 2020

@author: jtellier

NOTE: I modified this program for resubmission by FIXING the GCD logic check to work for all numbers,
and also added another function to take user input.
"""

"""function for finding the greatest common divisor
between two integers a and b. In this function, a must
be greater than b. """

#source code adapted from: https://www.w3resource.com/python-exercise/python-basic-exercise-31.php
def gcd(a, b):
    gcd=1
    
    if a % b == 0: #logical check
        return b
    
    for k in range(int(b/2),0,-1): #logical check using multiple modulus operators
        if a % k ==0 and b % k == 0:
            gcd=k
            break
    return gcd

gcd(15, 10) #testing the function
gcd(12,17)
gcd(4,6)
gcd(6,4)

def input_GCD():
    a = float(input("Enter first integer: ")) #Asking input from the user
    b = float(input("Enter second integer: "))
    print(gcd(a,b))
    
input_GCD() #checking input function
