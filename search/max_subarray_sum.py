import sys


def maximumSum(a, m):
    mx = 0
    a = [i%m for i in a]
    for i in range(1, len(a)):
        b = [sum(a[j:j+i])%m for j in range(len(a)-i+1)]
        x = max(b)
        if x > mx:
            mx = x
    return mx
    # Complete this function

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        a = list(map(int, input().strip().split(' ')))
        result = maximumSum(a, m)
        print(result)
