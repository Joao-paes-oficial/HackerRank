#!/bin/python3

import math
import os
import random
import re
import sys


def gameWithCells(n, m):
    return int((n + n % 2) * (m + m % 2) / 4)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
