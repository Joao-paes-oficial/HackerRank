import math
import os
import random
import re
import sys

def calculate(arr, i, j):
    a = arr[i][j]
    b = arr[i][j+1]
    c = arr[i][j+2]
    d = arr[i+1][j+1]
    e = arr[i+2][j]
    f = arr[i+2][j+1]
    g = arr[i+2][j+2]
    
    return (a+b+c+d+e+f+g)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
       
    new_arr = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            summ = calculate(arr, i, j)
            new_arr.append(summ)
    print(max(new_arr))