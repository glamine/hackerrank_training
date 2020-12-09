# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:36:20 2020

@author: guill
"""

def factorial(n):
    
    if n == 0:
        return 1
    
    else :
        return n*factorial(n-1)
    
def permutation(r,n):
    
    return factorial(n)/factorial(n - r)
    
def combination(r,n):
    
    num = factorial(n)
    denom = factorial(r) * factorial(n - r)
    
    return num/denom

def binomial(x,n,p):
    
    return combination(x, n) * p**x * (1 - p)**(n-x)
    
l, r = list(map(float, input().split(" ")))
proba = l / (l + r)
print(round(sum([binomial(i, 6, proba) for i in range(3, 7)]), 3))


##○ OR : SAME, from scipy ok
    
from scipy.stats import binom
   
print(round(sum([binom.pmf(i, 6, proba) for i in range(3, 7)]), 3))


#####################

perc, trials = list(map(int, input().split(" "))) # interessant !when using floats RUNTIME ERROR, better int !
proba = perc/100
print(round(sum([binomial(i, trials, proba) for i in range(3)]), 3)) # case 0 compris !
print(round(sum([binomial(i, trials, proba) for i in range(2, trials + 1)]), 3))