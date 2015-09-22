
from matplotlib.pyplot import *
import numpy as np 
from math import *

with open ('model_smg.dat') as file_name:
 
    x, y = np.float64(np.loadtxt(file_name, skiprows = 0, unpack=True))
    

with open ('ncounts_850.dat') as file_name:
    
    x1,y1 = np.float64(np.loadtxt(file_name, skiprows = 0, unpack=True))

    figure(0)
    plot(x1,y1,'ro')
    
    
def f_prime(x,y):
    h1 = x[i]-x[i-1]
    h2 = x[i+1]-x[i]
    return -(((h1/(h2*(h1+h2)))*(y[i+1])) - (((h1-h2)/(h2*h1))*(y[i])) - ((h2/(h1*(h1+h2)))*(y[i-1])))
    
for i in range (1,11):
    y2 = f_prime(x,y)
    print (y2)
    
    
    figure(1)
    plot(x1,y1,'ro')
    plot(log10(x[i]),log10(y2),'bo')
    xlabel("Luminosity")
    ylabel("Number of galexies above luminoisty")
    title("Graph of model data") 
