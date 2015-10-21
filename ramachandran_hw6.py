
# Derivative function

print("We need a f_prime function that only takes one variable. My original f_prime function took f_prime(x,y). This has been modified to only take the function that needs to be derived as a variable.")

def f_prime(y):
    def derivative(x, h=.1e-5):
        return( (y(x+h/2)-y(x-h/2))/h)
    return derivative 


#Black body function to test

print

def B(T):
    h = 6.626 * 10**(-27)
    c = 2.99 * 10**(10)
    wavelength = 0.087
    v = c/wavelength
    k = 1.380658 * 10**(-16)

    return (((2.0 * h * (v**3))/c**2)/(exp((h*v)/(k*T))-1.0)  - 1.25 * 10**(-12))

def Newton(x0, f, f_prime, tol = 1*10**(-15), N = 300):

    n = 1

    while n <= N:
        
        xi = x0 - (f(x0)/f_prime(x0))

        fxi = f(xi)

        if fxi <= tol:
            return xi
        else:
            x0 = xi

        #n += 1 

def bisection (f, a, b, i, tolerance) :
    
    fa = f(a)
    fb = f(b)
    
    if (fa * fb) > 0:
        print("a and b are not bracketing the roots")

        a = a * 1/2
        b = b * 2
                
    else:

        #print("a and b are bracketing the roots")

        i = 1 
        
        while (b-a)/2. > tolerance: 

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

def g(x):
    return (x**3) - x - 2
def y(x):
    return -6 + x + (x**2)

print("-----------------------------------------------------------")

print("This is to test the Newton function works")
print ("The root for g(x) by bisection is", bisection (g, 1, 2, 30, 0.001))
print("The root for g(x) by netwon is", Newton(6,g,f_prime(g)))
print ("The root for y(x) bisection is", bisection (y, 0, 5, 30, 0.001))
print("The root for y(x) by netwon is", Newton(6,y,f_prime(y)))

print("-----------------------------------------------------------")

print ("The root for B(T) by bisection is", bisection (B,10, 80, 100, 1*10**(-15)))
print("The root for B(T) by netwon is", Newton(80,B,f_prime(B)))

print("-----------------------------------------------------------")


if __name__ == "__main__":
    import timeit
    setup = "from __main__ import Newton, B, bisection,f_prime"
    print timeit.timeit("Newton(80,B,f_prime(B))", setup=setup)
    print timeit.timeit("bisection (B,10, 80, 100, 1*10**(-15))", setup=setup)

    print ("As we can see, the Newton function runs faster than the bisection function")


        