#!/usr/bin/env python
# Author: Paul Glenn
# Purpose:

##########################################
#  Imports
##########################################
import os
import sys
import shutil
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

##########################################
#  Setup
##########################################
dayOfTheWeek = 2

##########################################
#  Propagate from 1900 to 1901
#  Note that 1900 was not a leap year since
# Centuries must be divisible by 400
# to be leap years.
##########################################
dayOfTheWeek += 365
dayOfTheWeek = dayOfTheWeek%7 # reset to Januaryi 1st 1901
print(dayOfTheWeek) # so that day should be a tuesday

##########################################
#  Month Dictionary
##########################################
MonthKey = dict()
leapYear = 0
MonthKey[1] = 31
MonthKey[2] = 28 + leapYear
MonthKey[3] = 31
MonthKey[4] = 30
MonthKey[5] = 31
MonthKey[6] = 30
MonthKey[7] = 31
MonthKey[8] = 31
MonthKey[9] = 30
MonthKey[10] = 31
MonthKey[11] = 30
MonthKey[12] = 31


##########################################
#  keep track of Sundays
##########################################
numSundays  = 0

##########################################
#  Here we go...
##########################################

for year in range( 1901, 2001) :
    leapYear = 1 if year%4 == 0 else 0
    MonthKey[2] = 28 + leapYear
    # loop over months of the year
    for month in MonthKey.keys():
        # start on the first
        if dayOfTheWeek == 1 : numSundays += 1
        dayOfTheWeek += MonthKey[month]
        dayOfTheWeek = dayOfTheWeek%7

print (numSundays)



