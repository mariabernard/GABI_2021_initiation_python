#!/bin/env python3

#################################################################################
# Goal : compute simple mathematics metrics
#     - number of element
#     - sum
#     - mean
#     - standard deviation
#     - min
#     - max
#     - median
#
# Solution 1 : by computing it "manually", except for standard deviation for which you need to use the sqrt function of the "math" library
#
# Solution 2 : use dedicated function from math library
#
#################################################################################

## INPUT

# create a list of number (int) : list_number
list_number = [3, 4, 1, 5, 2]

#################################################################################

## SOLUTION 1

from math import *

# initialisation of metric : number of element, sum, min and max
# (some of them are needed to compute mean and sd)

                # TO COMPLETE


# parse list_number using a for loop and compute previous metrics

                # TO COMPLETE

# compute mean
                # TO COMPLETE

# compute standard deviation using sqrt() function
                # TO COMPLETE

# compute median
                # TO COMPLETE

# print results : 
#   Nombre=N Somme=S Moyenne=Mo SD=SD Min=Mi Max=Ma Mediane=Me

#################################################################################

## SOLUTION 2 : https://docs.python.org/3/library/statistics.html
from statistics import *

# print results : 
#   Nombre=N Somme=S Moyenne=Mo SD=SD Min=Mi Max=Ma Mediane=Me
