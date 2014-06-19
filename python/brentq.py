from math import tanh
from scipy.optimize import brentq

count = 0

def f(x):
    global count
    count+=1
    return tanh(x)

print brentq(f,-1.1,1.09,xtol = 10**-15.)
print count
