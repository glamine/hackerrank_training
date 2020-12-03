# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:34:05 2020

@author: guill
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def printMultiple(number):
    
    for i in range(10):
        
        res = number * (i + 1)
        
        msg = "{0} x {1} = {2}".format(number,i+1,res)
        #msg = "{num} x {times} = {result}".format(num=number,times=i+1,result=res)
        print(msg)


if __name__ == '__main__':
    n = int(input())
    printMultiple(n)