# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:30:51 2020

@author: guill
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def getLongestConsecOnes(n):
    
    length = 0
    currentLength = 0
    
    for i in range(n.bit_length()):
        
        if n & (1 << i):
            currentLength += 1
            length = max(length,currentLength)
        else:
            currentLength = 0
            
    
    return length 

if __name__ == '__main__':
    n = int(input())

    length = getLongestConsecOnes(n)
    print(length)
    
    # OR
    #print(max(map(len, bin(n)[2:].split('0')))) # get strings
    # functions hex, bin, len, map, split
    
    # OR also works by looking at odd values
    
    num = int(input())
    #Every odd values, Increment 1
    result = 0
    maximum = 0
    
    while num > 0:
        if num % 2 == 1:
            result += 1
            if result > maximum:
                maximum = result
    
        else:
            result = 0
        num //= 2
    print(maximum)
    
    
    
    
    