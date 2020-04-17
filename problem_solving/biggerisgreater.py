#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    s = list([ord(i) for i in w])
    for i in range(len(s)-1, 0, -1):
        if s[i] > s[i-1]:
            # swap i-1 and min(s[i:])
            _i = s[i:].index(min(filter(lambda _k : _k > s[i-1], s[i:]))) + i
            s[i-1], s[_i] = s[_i], s[i-1]
            _s = s[:i] + sorted(s[i:])
            return ''.join([chr(j) for j in _s])
    else:
        return 'no answer'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
