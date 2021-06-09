import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    
    result = 0
    for i in range(1, 11):
        result = n * i
        print('{} x {} = {}'.format(n,i,result))