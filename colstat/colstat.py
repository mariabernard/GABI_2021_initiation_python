#!/bin/env python3

#################################################################################
# Goal : compute simple mathematics metrics
#     - number of element
#     - sum
#     - mean
#     - min
#     - max
#     - median
#
# Solution 1 : by computing it "manually"
#
# Solution 2 : use dedicated function from statistics library : https://docs.python.org/3/library/statistics.html
#
#################################################################################

## INPUT

# create a list of number (int) : list_number
list_number = [3, 4, 1, 5, 2]

#################################################################################

## SOLUTION 1

# initialisation of metric : number of element, sum, min and max
# (some of them are needed to compute mean and sd)

                # TO COMPLETE


# parse list_number using a for loop and compute previous metrics

                # TO COMPLETE

# compute mean
                # TO COMPLETE

# compute median
                # TO COMPLETE

# print results : 
#   Nombre=N Somme=S Moyenne=Mo Min=Mi Max=Ma Mediane=Me

#################################################################################

## SOLUTION 2 : https://docs.python.org/3/library/statistics.html
from statistics import *

# print results : 
#   Nombre=N Somme=S Moyenne=Mo SD=SD Min=Mi Max=Ma Mediane=Me
