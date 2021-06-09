import os
import sys

#
# Complete the handshake function below.
#
def handshake(n):
    if n == 0 or n == 1:
        return 0
    counter = 0
    for i in range(n):
        counter += i
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()