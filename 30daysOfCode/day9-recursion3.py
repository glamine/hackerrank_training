# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:01:38 2020

@author: guill
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    
    nFac = 0
    
    if n <= 1:
        return 1
    else:
        return n*factorial(n - 1)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()