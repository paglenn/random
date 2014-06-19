# Monte Carlo simulation to estimate probability of random walk reaching
# the top  a  of a given interval [-b,a]
# Input: none (values of a and b specified in program code)
# Output: fraction of the total number of walks, that reached the top  a

from numpy import *
import numpy as np
from random import *

def walk_until_hit_boundary(a,b):
# simulates a random walk starting at W=0, walking
# in steps of size +1 or -1 each with probability 0.5
# until W hits a boundary of the interval [-b,a]
# ex/ walk_until_hit_boundary(5,2) simulates walk on [-2,5]
# Input: values of a and b (both positive integers)
# Output: value of W at the boundary (either -b or a)
# that it hits
    W=0
    while(W>-b and W<a):
       coinflip=np.random.randint(0,2) # returns 0 or 1, each equally probable
       s = 2*coinflip - 1 # s will be -1 or +1, each value with probability 0.5
       W=W+s
    print "W =",W
    return W
a=5; b=2
total_number_of_walks=0
number_of_walks_hit_a=0
for iwalk in range(100):
    total_number_of_walks+=1
    W=walk_until_hit_boundary(a,b)
    if(W > 0): # must be top boundary
       number_of_walks_hit_a+=1
print "number_of_walks_hit_a=",number_of_walks_hit_a
print "total_number_of_walks=",total_number_of_walks
print "fraction =",(1.*number_of_walks_hit_a)/total_number_of_walks
