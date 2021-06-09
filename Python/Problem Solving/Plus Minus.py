import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    negative_valor = 0
    neutral_valor = 0
    positive_valor = 0
    
    for i in range(len(arr)):
        if arr[i] < 0:
            negative_valor += 1
        elif arr[i] > 0:
            positive_valor += 1
        else:
            neutral_valor += 1
            
    print(positive_valor/len(arr))
    print(negative_valor/len(arr))
    print(neutral_valor/len(arr))
    
    
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
