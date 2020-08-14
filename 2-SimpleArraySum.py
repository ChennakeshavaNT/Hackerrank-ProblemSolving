#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(arr):
    #
    # Write your code here.
    sum = 0
    for num in arr:
        sum = sum + int(num)
    
    return str(sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    arr = input().split(" ")

    result = simpleArraySum(arr)

    fptr.write(result + '\n')

    fptr.close()
