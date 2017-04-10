#!/usr/bin/env python
# Author: Paul Glenn
# Purpose: To solve euler problem 152:
# There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.

# For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:

# In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it, the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.

#  How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers between 2 and 80 inclusive?

#################################################
# Imports
#################################################
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import os
import sys
import shutil
import copy

TopNum = 45
#################################################
# Dictionary with inverse square roots
#################################################
iSqr = {x: 1./(x*x) for x in range(2, TopNum+1)}
cumSum = dict()
for x in range( 2, TopNum + 1):
    xsum = 0
    for y in range(x,TopNum+1):
        xsum += iSqr[y]
    cumSum[x] = xsum
#print(cumSum)
    #cumSum[x] = sum
#cumSum = {x: sum(iSqr[x:-1]) for x in range(2,TopNum+1)}

#################################################
# what is equality?
#################################################s
def igual(x,y):
    diff = x - y
    eps = 3e-16
    if abs(x-y)< eps:
        return True
    else:
        return False

#################################################
# Now we need a recursive function to allow us to
# test successive numbers.
#################################################s
solutions = []

def AddToSqrtList(numList, num):
    sumList = sum([iSqr[x] for x in numList])
    #print(numList)
    #print(sumList)

    if igual(sumList, 0.5):
        print(numList)
        solutions.append(set(numList))
        return
    elif (sumList > 0.5) or num > TopNum:
        #print( numList, sumList)
        return
    elif sumList < 0.5:
        # define a useful range
        deficit = 0.5 - sumList
        #print(deficit)
        for x in range(num+1,TopNum+1):
            newList = numList + [x]
            if cumSum[num] >= deficit:
                AddToSqrtList(newList, x)
            else:
                return

AddToSqrtList([2],2)
print(solutions)
