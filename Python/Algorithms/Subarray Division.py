import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    output = 0
    if len(s) < m:
        return 0
    elif len(s) == 1 and s[0] == d:
        return m
    else:
        for i in range(0, len(s) - m + 1):
            for j in range (i, i + m):
                count += s[j]
            if count == d:
                output += 1    
                count = 0
            else:
                count = 0
    return output 
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()