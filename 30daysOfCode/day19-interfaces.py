# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:20:12 2021

@author: guill
"""

class AdvancedArithmetic(object):
    
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    
    def divisorSum(self, n):
        
        mySum = 0
        for i in range(n):
            
            if n % (i + 1) == 0:
                mySum += i + 1
        
        return mySum    


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)