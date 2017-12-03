def fib_array(n):
    a = [1, 2]
    while a[-1] < n:
        a.append(a[-1] + a[-2])
    del a[-1]
    return a

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum([i for i in fib_array(n) if i%2 == 0]))
