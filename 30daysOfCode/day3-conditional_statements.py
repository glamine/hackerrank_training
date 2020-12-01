# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:31:10 2020

@author: guill
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def isWeird(N):
    
    if N % 2 == 1:
        print("Weird")
    else:
        if N > 20 or (N <= 5 and N >= 2):
            print("Not Weird")
        else: 
            print("Weird")

if __name__ == '__main__':
    N = int(input())
    
    isWeird(N)