# Input:
# N - number of elements in list
# List of numbers to calculate weighted mean
# Weight of each number
# Output:
# Print weighted sum of elements in list
n = int(input())
w = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]

s = 0
for i in range(n):
    s += w[i]*l[i]
print(round(s/sum(l), 1))
