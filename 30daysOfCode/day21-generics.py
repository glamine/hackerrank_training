# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:08:06 2021

@author: guill
"""

from typing import TypeVar

Element = TypeVar("Element")


def printArray(array: [Element]):
    for element in array:
        print(element)


vInt = [1, 2, 3]
vString = ["Hello", "World"]

printArray(vInt)
printArray(vString)