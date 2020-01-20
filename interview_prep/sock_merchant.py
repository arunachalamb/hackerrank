import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    cntr = {} # dict to count occurences
    pairs = 0
    for i in range(n):
        if ar[i] in cntr:
            cntr[ar[i]] += 1
        else:
            cntr[ar[i]] = 1
    for k in cntr:
        pairs += cntr[k]//2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
