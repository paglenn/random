#!/usr/bin/env python
# Author: Paul Glenn
# Purpose: to solve the Euler problem of computing the first
# 10 digits of a sum of 100 fifty digit numbers in the file
# fiftydigitNumbers.txt

##########################################
# Imports
##########################################
import os
import sys
import shutil
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

##########################################
#  Read in the File fiftyDigitNumbers.txt
##########################################o
fin = open('fiftyDigitNumbers.txt','r')
lines = fin.readlines()
s = 0 # the sum
for line in lines:
    s += int(line[0:10])
    print(s)
