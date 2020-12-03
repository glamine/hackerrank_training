# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:45:11 2020

@author: guill
"""

from math import sqrt

def myMean(array, n):
    
    mean = sum(array)/n
    
    return round(mean,1) 

def myStd(array,n):
    
    mean = myMean(array,n)
    
    squaredSum = 0.0
    
    for i in range(n):
        
        squaredSum += (array[i] - mean)**2
    
    std = sqrt(squaredSum/n)
    
    return round(std,1)

nElem = int(input())
arrayString = input()

array = [int(s) for s in arrayString.split(' ')]


print(myStd(array,nElem))

################################§

def myMedian(array, n):
    
    array.sort()
    i = n // 2
    
    if n % 2 == 0:
        median = (array[i - 1] + array[i])/2.0
    else:
        median = array[i]
    
    return round(median,1)


def myQuartiles(array,n):
    
    q2 = int(myMedian(array, n))
    
    L = [elem for elem in array if elem < q2]
    R = [elem for elem in array if elem > q2]

    q1 = int(myMedian(L,len(L)))
    q3 = int(myMedian(R,len(R)))
    
    
    return q1, q2, q3

nElem = int(input())
arrayString = input()

array = [int(s) for s in arrayString.split(' ')]


q1, q2, q3 = myQuartiles(array,nElem)

print(q1)
print(q2)
print(q3)