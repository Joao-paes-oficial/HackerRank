#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    U = D = 0
    for i in range(steps):
        if(path[i] == 'U'):
            D += 1
            if(D == 0):
                U += 1
        else:
            D -= 1
    return U
                    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
