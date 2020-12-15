# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:43:31 2020

@author: guill
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    
    def computeDifference(self):
        
        maxDiff = 0
        
        for i in range(len(self.__elements)):
            
            for j in range(len(self.__elements)):
                
                maxDiff = max(abs(self.__elements[i] - self.__elements[j]),maxDiff)
        
        self.maximumDifference = maxDiff
    
    # OR : quicker?
# =============================================================================
#     def computeDifference(self):
#         
#         maxValue = max(a)
#         minValue = min(a)
#         self.maximumDifference = maxValue - minValue
# =============================================================================

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)