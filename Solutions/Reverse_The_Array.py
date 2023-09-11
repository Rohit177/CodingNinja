from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, pos):
    if pos >= len(arr):
        return arr  
    part1 = arr[:pos+1]
    part2 = arr[pos+1:]

    part2.reverse()

    return part1 + part2


