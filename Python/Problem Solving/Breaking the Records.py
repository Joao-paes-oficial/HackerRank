import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxi = scores[0]
    mini = scores[0]
    counter_maxi = 0
    counter_mini = 0
    for i in range(len(scores)):
        if scores[i] > maxi:
            maxi = scores[i]
            counter_maxi += 1
        if scores[i] < mini:
            mini = scores[i]
            counter_mini += 1
    return counter_maxi, counter_mini
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()