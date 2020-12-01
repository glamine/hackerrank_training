# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:06:08 2020

@author: guill
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    
    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    #totalCost = int(meal_cost + tip + tax)
    totalCost = round(meal_cost + tip + tax)
    
    print(totalCost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)