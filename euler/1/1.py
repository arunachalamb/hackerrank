t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    r3 = (n-1)%3
    n3 = (n-1)-r3
    n3 = n3//3
    m3 = (3*n3*(n3+1))//2
    r5 = (n-1)%5
    n5 = (n-1)-r5
    n5 = n5//5
    m5 = (5*n5*(n5+1))//2
    r15 = (n-1)%15
    n15 = (n-1)-r15
    n15 = n15//15
    m15 = (15*n15*(n15+1))//2
    print(m3+m5-m15)
