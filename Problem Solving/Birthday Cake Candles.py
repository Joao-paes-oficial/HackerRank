import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    counter = 1
    new_list = []
    for i in range(len(candles)):
        if candles[i] in new_list:
            counter += 1
        else:
            new_list.append(candles[i])
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()