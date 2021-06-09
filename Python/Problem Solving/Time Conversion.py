import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    new = s.split(":")
    
    if s[-2:] == "PM":
        if new[0] != "12":
            new[0] = str(int(new[0])+12)
    else:
        if new[0] == "12":
            new[0] = "00"
    new_time = ':'.join(new)
    return str(new_time[:-2])
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
