#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    _min = math.inf
    _max = 0

    _d = dict()
    for j in genes:
        _d[j] = re.compile(r'(?=({_j}))'.format(_j=j))

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        _h = health[first:last+1]
        _g = genes[first:last+1]
        _s = 0
        #print(d)
        #print(_g)
        for i, j in enumerate(_g):
            _s += len(re.findall(_d[j], d))*_h[i]
            #print(j, _h[i], _s)
        if _s < _min:
            _min = _s
        if _s > _max:
            _max = _s
        #print(_min, _max)
    print(_min, _max)



