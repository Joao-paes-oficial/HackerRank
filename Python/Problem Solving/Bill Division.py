import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum_arr = 0
    new_arr = []
    for i in range(len(bill)):
        if i == k:
            new_arr.append(0)
        else:
            new_arr.append(bill[i])
    
    sum_arr = int(abs((sum(new_arr)/2) - b))
      
    if sum_arr == 0:
        print('Bon Appetit')
    else:
        print(sum_arr)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)