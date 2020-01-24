#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:42:56 2020

@author: jtellier
"""
#A function to draw flowers with any given number of petals

import turtle #import turtle graphical drawing module
import math #import math functions
bob = turtle.Turtle() #define bob as a drawing turtle

def polyline(t, n, length, angle):
    """draws n line segments with the given length and 
    angle (in degrees) between them. t is a turtle. """
    for i in range(n):
        t.fd(length) #defines the length that the turtle should travel
        t.lt(angle) #defines the angle that the turtle should turn after travelling

def petal(t, r, angle):
    """converts the line segment into an arc of length r
    that doubles back on itself in order to draw a closed
    petal if angle is set to 90"""
    arc_length = 2*math.pi*r*angle/360 #defining the length of the arc
    n = int(arc_length/3)+1 #determines how many times to repeat polyline function
    step_length = arc_length/n #length of one side of petal
    step_angle = float(angle)/n #angle of one side of petal
    polyline(t, n, step_length, step_angle) #draw one side of petal
    t.lt(270) #turn to face the correct orientation for drawing closed figure
    polyline(t, n, -step_length, step_angle) #draw other side of petal
    t.lt(-90) #turn to reset orientation

def flower(t, x):
    """draws a flower with x number of sides using turtle t"""
    for i in range(x):
        petal(t, 50, 90) #calling petal function
        t.lt(360/x) #turn the turtle the correct angle for the number of petals

flower(bob, 12) #example flower with 12 sides
