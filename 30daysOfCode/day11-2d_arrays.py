# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:38:33 2020

@author: guill
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def getSumHourGlass(arr,idGlassCol,idGlassRow):
    
    mySum = -1000 # attention, could be negative sum !!
    
    mySum = arr[0 + idGlassRow][0 + idGlassCol] + arr[0 + idGlassRow][1 + idGlassCol] \
        + arr[0 + idGlassRow][2 + idGlassCol] + arr[1 + idGlassRow][1 + idGlassCol] \
        + arr[2 + idGlassRow][0 + idGlassCol] + arr[2 + idGlassRow][1 + idGlassCol] \
        + arr[2 + idGlassRow][2 + idGlassCol]  # ligne - colonne
    
    return mySum
    

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
      
    maxSum = -1000
    currentSum = -1000
      
    for i in range(4):
        
        for j in range(4):
            
            currentSum = getSumHourGlass(arr,i,j)
            maxSum = max(currentSum,maxSum)
            
    print(maxSum)