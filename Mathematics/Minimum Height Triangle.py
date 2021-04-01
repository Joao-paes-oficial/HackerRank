import math
import sys

def lowestTriangle(base, area):
    return math.ceil(2*area/base)
    #math.ceil serve para aproximar o valor

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)