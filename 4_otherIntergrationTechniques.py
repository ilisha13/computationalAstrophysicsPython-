
"""Intergration using peicewise linear method, trapezoidal intergrator, and Simpson's rule"""

import numpy as np
import math as math 


def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i+= step

def trapRule (a,b,f):
    total = 0.
    h = (b-a)/2
    for i in frange(a,b,0.01):
        area =.01*(f(i+.01)+f(i))/2.0
        """print(area)"""
        total = total + area
    return total

def midPoint(a,b,f):
    total = 0
    for i in frange(a,b,.01):
        area = .01*(f((i+(i+.01))/2))
        total = total + area
    return total

def simpson(a,b,f):
    total = 0
    for i in frange(a,b,.01):
        area = (.01/6)*(f(i)+4*f((i+(i+.01))/2)+f(i+.01))
        total = total + area
    return total



def f(x):
    return (x**3+(2*x**2)-4)

print("Trap rule = ", trapRule(-1,1,f))
print("Midpoint = ", midPoint(-1,1,f))
print ("Simpson = ", simpson(-1,1,f))

print ("Gaussian method in special case of interval [-1,1]",f(-1/(math.sqrt(3)))+f(1/(math.sqrt(3))))

print("The error on all of these values is less than 1% from the original.")
