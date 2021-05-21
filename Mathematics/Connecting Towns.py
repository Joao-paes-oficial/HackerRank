#!/bin/python3

import math
import os
import random
import re
import sys


def connectingTowns(n, routes):
    p = 1
    for x in range(n - 1):
        p = p * routes[x]
    return p % 1234567

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
