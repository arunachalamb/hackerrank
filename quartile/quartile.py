# Input:
# N - number of elements in list
# List of elements
# Output:
# Print first, second and third quartile of elements
n = int(input())
l = [int(i) for i in input().split()]
l.sort()

def median(p, n):
    if n%2 == 1:
        return p[n//2]
    else:
        return (p[n//2] + p[n//2-1])/2

if n%2 == 1:
    q2 = l[n//2]
    q1 = median(l[:n//2],n//2)
    q3 = median(l[n//2+1:],n//2)
else:
    q2 = (l[n//2] + l[n//2-1])/2
    if n/2 % 2 == 1:
        q1 = l[n//2//2]
        q3 = l[n//2 + n//2//2]
    else:
        q1 = median(l[:n//2], n//2)
        q3 = median(l[n//2:], n//2)
print(int(round(q1,0)))
print(int(round(q2,0)))
print(int(round(q3,0)))
