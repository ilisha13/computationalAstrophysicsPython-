
""" Using a given model of data, write a code to convert the absolute model number to differential counts, and 
plot the observed data against the model. """

from matplotlib.pyplot import *
import numpy as np 
from math import *


#Imports the model values
with open ('model_smg.dat') as file_name:
 
    x, y = np.float64(np.loadtxt(file_name, skiprows = 0, unpack=True))
    
#Imports the observed values 
with open ('ncounts_850.dat') as file_name:
    
    x1,y1 = np.float64(np.loadtxt(file_name, skiprows = 0, unpack=True))

    figure(0)
    plot(x1,y1,'ro')
    
#The equation for finding dN/dL from the model values. Returns dN/dL    
def f_prime(x,y):
    h1 = x[i]-x[i-1]
    h2 = x[i+1]-x[i]
    return -(((h1/(h2*(h1+h2)))*(y[i+1])) - (((h1-h2)/(h2*h1))*(y[i])) - ((h2/(h1*(h1+h2)))*(y[i-1])))


#Makes a list of dN/dL for the values of x that does not include first and last value. Also log10 values.
model_dN_dL = list()

for i in range (1,11):
    y2 = f_prime(x,y)
    print (y2)
    log_lumi = np.log10(y2)
    model_dN_dL.append(log_lumi)

#Logs the luminosity values and cuts off first and last value 

lumi = np.log10(x[1:-1])

#Plots model data vs observed data 

figure(0)
plot(x1,y1,'ro',label = "Observed Data")
plot(lumi,model_dN_dL,'bo',label = "Model Data")
xlabel("Log of Luminosity")
ylabel("Log of Number of galexies above luminoisty")
title("Graph of Model Data vs Observed Data")
legend(numpoints=1)
show()
savefig()
