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

##############################

def setFromFrequency(array,frequency,n):
    
    fullSet = []
    
    for i in range(n):
        
        for j in range(frequency[i]):
        
            fullSet.append(array[i])
    
    return fullSet

def interQuartilesRange(array,frequency,n):
    
    fullSet = setFromFrequency(array, frequency, n)
    
    q1, q2, q3 = myQuartiles(fullSet,sum(frequency))
    
    IQrange = q3 - q1
    
    return round(IQrange,1)

nElem = int(input())
arrayString = input()
freqString = input()

array = [int(s) for s in arrayString.split(' ')]
freq = [int(s) for s in freqString.split(' ')]


print(interQuartilesRange(array,freq,nElem))


####################################"

# Define functions
def median(size, values):
    if size % 2 == 0:
        median = (values[int(size/2)-1] + values[int(size/2)]) / 2
    else:
        median = float(values[int(size/2)])
    return median

# Set the data
size = int(input())
elements = list(map(int, input().split()))
frequencies = list(map(int, input().split()))

new_data = []
for i in range(len(elements)):
    for j in range(frequencies[i]):
        new_data.append(elements[i])
new_data = sorted(new_data)

# Verify that the total data is even or odd
size = int(len(new_data))
if size % 2 == 0:
    data_low = new_data[0:int(size/2)]
    data_high = new_data[int(size/2):size]
else:
    data_low = new_data[0:int(size/2)]
    data_high = new_data[int(size/2)+1:size]

# Get the final result and print on the screen
low = median(len(data_low), data_low)
high = median(len(data_high), data_high)
print(high - low)