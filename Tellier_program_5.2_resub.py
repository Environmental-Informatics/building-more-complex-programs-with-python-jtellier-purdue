#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:11:44 2020

@author: jtellier

NOTE: Added full header block in this resubmission.

This program was created by Joshua Tellier of Purdue University. The purpose of this program is to 
create functions that check fermat's theorem and allow the user to input numbers to check the theorem as well.
"""

"""Two functions that check Fermat's theorem. One 
that prompts the user, the other requires input"""
def check_fermat(a, b, c, n):
    if n > 2 and (a**n) + (b**n) == (c**n): #conditional for Fermat's theorem
        print('Holy smokes, Fermat was wrong!') #what to print if condition is true
    else:
        print("No, that doesn't work.") #what to print if condition is  false
        
check_fermat(2,3,3,3) #testing the function

def input_fermat():
    a = float(input("Enter a: ")) #Asking input from the user
    a = int(a) #converting user input to an integer
    b = float(input("Enter b: "))
    b = int(b)
    c = float(input("Enter c: "))
    c = int(c)
    n = float(input("Enter n: "))
    n = int(n)
    check_fermat(a, b, c, n) #applying user inputs to the check_fermat function
    
input_fermat() #testing the function
