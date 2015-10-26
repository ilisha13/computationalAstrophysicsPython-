"""Step 1: we want to pick a and b, so that f(a) and f(b) have opposite signs. 
Step 2: Find the midpoint c = (a+b)/2 of these points. If f(c) = close to 0,root found. 
If not, 
 - If f(a) and f(c) have opposite signs, then this is a new bracket. Restart process with a = a and b = c. 
 - If f(c) and f(b) have opposite signs, then this is a new bracket. Restart process with b = b and a = c. """

# printing out steps:

print("The bisection function has five inputs: f, a, b, i and tolerance. f is the function we want to find the roots of, a and b are our random values that hopefully bracket the root, i is the maximum number of iterations we want before the loop stops looping, and tolerance is our chosen tolerance level. We first want to make sure that we have picked an a and b value that is bracketing the roots. To do test this, we multiply f(a) and f(b) together and see whether this resulting value is positive or not. If they have oppsite signs (and thus are bracketing the root), they should be negative when multiplied together. This is done using the 'if' statement. If they are not bracketing the root, then a is halved and b is doubled. If they are bracketing the root, we need to make them get closer and closer until the tolerance level or zero is reached by one of them. This is done in the 'while' loop and subsequent 'if' statements.")





# Importing the necessary libraries 

import numpy as np
import matplotlib.pyplot as plt

"""The inputs for this bisection function are f (the function we want to find the root of), 
   a and b (our random values that hopefully bracket the root), 
   i (the maximum number of iterations we want before the loop gives up), 
   and our chosen tolerance level."""

def bisection (f, a, b, i, tolerance) :
    
    fa = f(a)
    fb = f(b)
    
#To make sure f(a) and f(b) have opposite signs, 
#we can test whether when they multiply together, they are positive or not. 
#If they have opposite signs, they should always be negative when mulitplied together.
    
    if (fa * fb) > 0:
        print("a and b are not bracketing the roots")

        # Now we need to change the roots to find a bracketing value. In this case, I will half the a value and double the b value.
        a = a * 1/2
        b = b * 2
                
    else:

        print("a and b are bracketing the roots")

        i = 1 
        
        while (b-a)/2. > tolerance: # so we know the roots aren't within our tolerance level. 

            c = (b+a)/2.
            
            fc = f(c)

            if 0 <= fc <= tolerance:
                return c
            
            elif fc * fa < 0:
                b = c
              
            else:
                a = c
               
            i += 1

        return c

def f(x):
    return np.sin(x)

def g(x):
    return (x**3) - x - 2

def y(x):
    return -6 + x + (x**2)
        
# Prints the roots of the above three functions
print ("The root for f(x) is", bisection(f, 2, 4, 30, 0.001))
print ("The root for g(x) is", bisection (g, 1, 2, 30, 0.001))
print ("The root for y(x) is", bisection (y, 0, 5, 30, 0.001))

# Graphs the above three functions to see where the roots are visually

# This creates an array of x values

t = np.arange(0, 5, 0.1);

plt.ylim([0, 8])
plt.plot( t, f(t), 'b', label =  "f(x)")
plt.plot( t, g(t), 'g', label =  "g(x)")
plt.plot( t, y(t), 'm', label =  "y(x)")
plt.legend()

plt.show()
plt.savefig()
