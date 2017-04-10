#!/usr/bin/env python
# Author: Paul Glenn
# Purpose: To solve the euler problem:
# How many 18-digit numbers n (without leading zeros) are
# there such that no digit occurs more than
# three times in n?

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import os
import sys
import shutil

##########################################
# First a function to convert a # to a list of its digits
##########################################
def digits(num):
    s = str(num)
    L = list(s)
    listOfNumbers = [int(l) for l in L]
    return listOfNumbers

##########################################
#Brute-Force Algorithm
##########################################

counter = 0
start = int(1e17)
end = int(1e18)
for num in range(start,end):
    numDigits = digits(num)
    numDict = {x:numDigits.count(x) for x in numDigits}
    if len(numDict.keys()) >  6:
        if max(numDict.values()) < 3 :
            counter += 1


print(counter)

