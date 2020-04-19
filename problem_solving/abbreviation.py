#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    _a = set(i for i in list(a) if i.isupper())
    _b = set(b.upper())
    if not _a.issubset(_b):
        print(a, b, _a, _b, 'NO')
        return 'NO'

    _r = '.*'.join(list(b))
    _rs = re.findall(_r, a.upper())
    if len(_rs) > 0:
        print(a, b, _rs, len(_rs), 'YES')
        return 'YES'
    print(a, b, _rs, len(_rs), 'NO')
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
