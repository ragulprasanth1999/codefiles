from sys import *
from collections import *
from math import *

def rotateArray(arr):
    v = arr[0] 
    arr.pop(0)  
    arr.append(v)  
    return arr
