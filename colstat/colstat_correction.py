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
N = 0
Sum = 0
Min = None
Max = None

# parse list_number using a for loop and compute previous metrics
for number in list_number:
    N = N + 1
    Sum = Sum + number
    if Min == None:
        Min = number
    elif number < Min:
        Min = number
    if Max == None:
        Max = number
    elif number > Max:
        Max = number

# compute mean
Mean = Sum / N

# compute standard deviation using sqrt() function
sum_deviation = 0
for number in list_number:
    sum_deviation = sum_deviation + ((number - Mean) * (number - Mean))
SD = round(sqrt(sum_deviation / N), 2)

# compute median
list_number.sort()
Median = list_number[int(N / 2)]

# print results : 
#   Nombre=N Somme=S Moyenne=Mo SD=SD Min=Mi Max=Ma Mediane=Me
print("Nombre=" + str(N) + " Somme=" + str(Sum) + " Moyenne=" + str(Mean) +
      " SD=" + str(SD) + " Min=" + str(Min) + " Max=" + str(Max) +
      " Mediane=" + str(Median) + "\n")

#################################################################################

## SOLUTION 2 : https://docs.python.org/3/library/statistics.html
from statistics import *

N=len(list_number)
Sum=sum(list_number)
Mean=mean(list_number)
SD=round(pstdev(list_number),2)
Min=min(list_number)
Max=max(list_number)
Median = median(list_number)

print("Nombre=" + str(N) + " Somme=" + str(Sum) + " Moyenne=" + str(Mean) +
      " SD=" + str(SD) + " Min=" + str(Min) + " Max=" + str(Max) +
      " Mediane=" + str(Median) + "\n")
