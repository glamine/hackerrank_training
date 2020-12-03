# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:58:36 2020

@author: guill
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from statistics import mode
from collections import Counter 


def myMean(array, n):
    
    mean = sum(array)/n
    
    return round(mean,1) 

def myMedian(array, n):
    
    array.sort()
    i = n // 2
    
    if n % 2 == 0:
        median = (array[i - 1] + array[i])/2.0
    else:
        median = array[i]
    
    return round(median,1)
    
def myMode(array):
    
    data = Counter(array) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    
    if len(mode) != 1: 
        min_mode = min(mode)

    return min_mode

nElem = int(input())
arrayString = input()

array = [int(s) for s in arrayString.split(' ')]


print(myMean(array,nElem))
print(myMedian(array,nElem))
print(myMode(array))

###########

def myWeightedMean(array, weights, n):
    
    weightedSum = 0.0
    
    for i in range(n):
        
        weightedSum += weights[i]*array[i]
    
    mean_w = weightedSum/sum(weights)
    
    return round(mean_w,1) 

nElem = int(input())
arrayString = input()
weightsString = input()

array = [int(s) for s in arrayString.split(' ')]
weights = [int(s) for s in weightsString.split(' ')]


print(myWeightedMean(array,weights,nElem))


