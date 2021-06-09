#!/bin/python3

import math
import os
import random
import re
import sys


def summingSeries(n):
    
    return n ** 2 % (10 ** 9 + 7)

if __name__ == '__main__': 
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
