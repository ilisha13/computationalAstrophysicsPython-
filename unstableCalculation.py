""" Implement the recurrence relation for various functions. Calculate the relative and absolute
     errors for each calculation. Based on these errors, determine whether the calculation is stable or not. """



import numpy as np
from math import *
"""                 Part 1                

     Consider the recurrence relation xn = (1/3)**n             """


for n in range (0,21):
    
    xBar = np.float32((3**(-1))**n)
    xReal = np.float64((3**(-1))**n)
    absolute = np.float64(xReal - xBar)
    relative = np.float64(absolute/xReal)
    
    #prints values of x when n = 0,1,2,3,4,5 
    if n in range (0,6): 
        print "When n = ", n,", x =", xBar  

    #prints absolute and relative values when x = 5 
    if n == 5:  
        print "The absolute error when x = 5 is ", absolute
        print "The relative error when x = 5 is ", relative

    #prints absolute and relative values when x = 20
    if n == 20: 
        print "The absolute error when x = 20 is ", absolute
        print "The relative error when x = 20 is ", relative
        
"""We can see that there is a large difference between the absolute
 errors when x=5 and x=20, but not a big difference between the relative
 errors of the two.""" 

        
"""                 Part 2                

     Consider the recurrence relation xn = 4**n             """


for n in range (0,21):
    
    xBar = np.float32(4**n)
    xReal = np.float64(4**n)
    absolute = np.float64(xReal - xBar)
    relative = np.float64(absolute/xReal)
    
    #prints values of x when n = 0,1,2,3,4,5 
    if n in range (0,6): 
        print "When n = ", n,", x =", xBar  

    #prints absolute and relative values when x = 5 
    if n == 5:  
        print "The absolute error when x = 5 is ", absolute
        print "The relative error when x = 5 is ", relative

    #prints absolute and relative values when x = 20
    if n == 20: 
        print "The absolute error when x = 20 is ", absolute
        print "The relative error when x = 20 is ", relative

"""This is a stable calculation because the values used are integer
 values rather than floats. The errors produced are 0, so this proves
 that the calculation is stable.""" 

"""                 Part 3                

     Proving that it works              """

x = np.float64(10**200)
y = np.float32(10**200)
print x
print y
