from datetime import datetime
from datetime import timedelta

t1 = datetime.now()
t2 = datetime.now()

# Derivative function
def f_prime(x,y):
    h1 = x[i]-x[i-1]
    h2 = x[i+1]-x[i]
    return -(((h1/(h2*(h1+h2)))*(y[i+1])) - (((h1-h2)/(h2*h1))*(y[i])) - ((h2/(h1*(h1+h2)))*(y[i-1])))

#Black body function to test 

def B(T):
    h = 6.626 * 10**(-27)
    c = 2.99 * 10**(10)
    v = 
    k = 1.380658 * 10**(-16)

def Newton(x0, f, f_prime, tol = 0.001, N = 300):

    n = 1

    while n <= N:
        
        xi = x0 - (f(x0)/f_prime(x0))

        fxi = f(xi)

        if fxi <= tol:
            return xi
        else:
            x0 = xi

    n = n+1 

        