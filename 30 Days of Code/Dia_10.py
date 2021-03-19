import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = str(bin(int(input())))
    number_string = n[2:]
    counter = 0
    maxi = 0
    i = 0
    
    while i < len(number_string):
        if number_string[i] == "1":
            counter += 1
        else:
            counter = 0
        
        if counter > maxi:
            maxi = counter
        
        i += 1
        
    print(maxi)