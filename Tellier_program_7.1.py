#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:53:59 2020

@author: jtellier
"""

"""This contains two functions, one of which uses 
newtons method to calculate square root, and the
other which reproduces a table like the one seen
in exercise 7.1"""

import math #math module necessary for math.sqrt
def mysqrt(a):
    x = math.sqrt(a) + 4 #creating x, a reasonably close estimate of sqrt(a)
    while True:
        y = (x + a/x)/2 #newtons method formula
        if abs(y-x) < 0.0000001: #if the difference between the current iteration and 
            #the actual value is less than the threshold, 
            return(x) #the number is printed, must use return(), not print() to get it to work
            break #and the loop ends
        x = y

mysqrt(2) #testing function

def test_square_root():
    for i in range(1, 9): 
        print('%-12i%-12g%-12g%-12g' % (i,mysqrt(i),math.sqrt(i),(abs(mysqrt(i)-math.sqrt(i)))))
"""this function uses string formatting to display the integer,
the square root based on newtons method, the actual square root,
and the difference between the two for the integers 1-9 in the
 console window in table format"""
 
test_square_root() #testing function

