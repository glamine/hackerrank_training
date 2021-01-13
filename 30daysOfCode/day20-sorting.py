# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:32:25 2021

@author: guill
"""

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here


totalSwaps = 0

for i in range(n):
    
    numberOfSwaps = 0
    
    for j in range(n - 1):
        
        if a[j] > a[j + 1]:
            
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1
        
    totalSwaps += numberOfSwaps
            
    if numberOfSwaps == 0:
        break
s = "Array is sorted in {0} swaps.".format(totalSwaps)
s1 = "First Element: {0}".format(a[0])
s2 = "Last Element: {0}".format(a[-1])
 
print(s)
print(s1)
print(s2)

# algorithm for bubble sort
# =============================================================================
# for (int i = 0; i < n; i++) {
#     // Track number of elements swapped during a single array traversal
#     int numberOfSwaps = 0;
#     
#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#             numberOfSwaps++;
#         }
#     }
#     
#     // If no elements were swapped during a traversal, array is sorted
#     if (numberOfSwaps == 0) {
#         break;
#     }
# }
# =============================================================================
