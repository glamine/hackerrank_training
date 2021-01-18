# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:19:59 2021

@author: guill
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

def isPrimal(n):

    if n == 1 or n == 2 or n == 3:
        return True
    else:
        for i in range(2,int(sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

T=int(input())

for i in range(T):
    
    num = int(input())
    
    if num >= 2 and isPrimal(num):
        print("Prime")
    else:
        print("Not prime")