# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:51:02 2020

@author: guill
"""


def indexSplit(myString):
    
    resultStr = ""
    evenStr = ""
    oddStr = ""
    
    for i in range(len(myString)):
        
        if i % 2 == 0:
            
            evenStr += myString[i]
            
        else:
            
            oddStr += myString[i]
                
    resultStr = evenStr + " " + oddStr
    
    print(resultStr)


if __name__ == '__main__':
    
    n = int(input())
    
    for i in range(n):
        
        currentString = input()
        indexSplit(currentString)
