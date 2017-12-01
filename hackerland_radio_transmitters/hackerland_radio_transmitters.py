import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]

x = sorted(x)
a = 0
v = x[a] + k
N = 1
for i in range(0, len(x)):
    if x[i] <= v:
        a = i
    elif x[i] > x[a] + k:
        N += 1
        a = i
        v = x[a] + k
print(N)
