# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:19:55 2020

@author: guill
"""

def printReverse(myArray):
    
    reverseStr = str(myArray[0])
    
    for i in range(1,len(myArray)):
        
        reverseStr = str(myArray[i]) + " " + reverseStr
    
    print(reverseStr)

if __name__ == '__main__':
    
    nElem = int(input())
    arrayString = input()
    
    array = [int(s) for s in arrayString.split(' ')]
    
    printReverse(array)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    printReverse(arr)
    