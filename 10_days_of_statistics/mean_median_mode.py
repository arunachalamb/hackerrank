# Input:
# N - number of elements in list
# Input list to calculate mean, median, mode
# Output:
# Print mean, median and mode of elements in list
n = int(input())
l = [int(i) for i in input().split()]

print(sum(l)/n)
l.sort()
if n%2 == 1:
    print(l[n//2])
else:
    print((l[n//2-1]+l[n//2])/2)
m = [0 for i in range(n)]
for i in range(n):
    m[i] = l.count(l[i])
print(l[m.index(max(m))])
