
"""Create an intergration function and apply it to the angular diameter distance in cosmology"""

import numpy as np
import math 
from matplotlib.pyplot import *


#Trapizoidal rule
 
def trapRule (a,b,f):
    total = 0.
    h = (b-a)/2
    for i in frange(a,b,0.01):
        area =.01*(f(i+.01)+f(i))/2.0
        """print(area)"""
        total = total + area
    return total

"""Python 2 does not do ranges like python 3 does! I couldn't put a float in the step. So this frange function allows me to write a range with float steps. I was stuck on this part for so long!"""

def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i+= step

def r(z):
    Q_m = (0.3)
    Q_v = (0.7)
    Q_r = 0
    C = (3*(10**3))

    return ((C/(math.sqrt((Q_m*((1+z)**3))+(Q_r*((1+z)**2))+Q_v))))

def D(z):
    return (trapRule(0,z,r)/(1+z))

"""runs through z values from 0 to 5"""

values = []
for i in range (6):
    values.append(D(i))

    
"""Plots graph"""

plot(values)
title("Graph showing Da vs z")
    
show()


    







    




