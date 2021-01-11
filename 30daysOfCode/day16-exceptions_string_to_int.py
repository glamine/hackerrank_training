# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:18:22 2021

@author: guill
"""

#!/bin/python3

import sys


S = input().strip()

try:
    
    number = int(S)
    print(number)
    
except ValueError:
    
    print("Bad String")