import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    x = 0
    for i in ar:
        x += i
    return x    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()