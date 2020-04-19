#!/bin/python3

import math
import os
import random
import re
import sys

HOUR = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen', 'twenty']
NUM = [i for i in range(1, 21)]
NUM2WORD = dict(zip(NUM, HOUR))
NUM2WORDSP = { 0 : "o' clock", 15 : 'quarter past', 30 : 'half past', 45 : 'quarter to'}

# Complete the timeInWords function below.
def timeInWords(h, m):
    if m == 0:
        return NUM2WORD[h] + ' ' + NUM2WORDSP[0]
    elif m == 15 or m == 30:
        return NUM2WORDSP[m] + ' ' + NUM2WORD[h]
    elif m == 45:
        return NUM2WORDSP[m] + ' ' + NUM2WORD[h+1]
    elif m == 1:
        return NUM2WORD[m] + ' minute past ' + NUM2WORD[h]
    elif m > 1 and m <= 20:
        return NUM2WORD[m] + ' minutes past ' + NUM2WORD[h]
    elif m > 20 and m < 30:
        return 'twenty ' + NUM2WORD[m%10] + ' minutes past ' + NUM2WORD[h]
    elif m > 30 and m < 40:
        return 'twenty ' + NUM2WORD[10 - m%10] + ' minutes to ' + NUM2WORD[h+1]
    elif m >= 40 and m < 59:
        return NUM2WORD[60 - m] + ' minutes to ' + NUM2WORD[h+1]
    elif m == 59:
        return NUM2WORD[60 - m] + ' minute to ' + NUM2WORD[h+1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

