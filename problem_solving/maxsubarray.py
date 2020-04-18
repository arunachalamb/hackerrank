#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    _sum = sum(arr)
    _mseq = sum([i for i in arr if i > 0])
    if _mseq == 0:
        _mseq = max(arr)
        return (_mseq, _mseq)
    _cs = 0
    _bs = 0
    for i in arr:
        _cs = max(0, _cs+i)
        _bs = max(_bs, _cs)
        #print(i, _cs, _bs)
    return (_bs, _mseq)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

