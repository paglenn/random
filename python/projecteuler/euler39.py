#!/usr/bin/env python
# Author: Paul Glenn
# Purpose: To solve euler problem #39:
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import os
import sys
import shutil

#################################################
# What is equality?
#################################################

def igual(x,y):
    diff = x - y
    eps = 2e-16
    if abs(x-y)< eps:
        return True
    else:
        return False

def isPerfectSquare(num):
    sqrtNum = math.sqrt(num)
    trunc = int(sqrtNum)
    if igual(sqrtNum, trunc):
        return True
    else:

        return False

#################################################
# Set up the equations for any choice of p
#################################################

numSolutions = []
for p in range( 1,1000) :
    solutions = []
    for u in range(1, p):
        u2 = u*u
        v = 0.5 * ( u2 - ( p - u) **2 )
        if v > 0 and igual(v, int(v)):
            c2 = u2 - 2*v
            if isPerfectSquare(c2):
                c = math.sqrt(c2)
                discriminant = c2 - 2 * v
                if discriminant >= 0:
                    b = 0.5 * ( u + math.sqrt(c2 - 2*v))
                    a = u - b
                    if igual(a, int(a)) and igual(b, int(b)):
                        solutions.append({a,b,c})

    numSolutions.append(len(solutions))
    if p == 120:
        print("The index of p = 120 is", len(numSolutions) - 1)
        print("The length of the set for  p = 120 is", len(solutions))
print("Maximum number of solutions is at", numSolutions.index(max(numSolutions))+1)


