n = int(input().strip())
N = n
i = 2
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
if n == N:
    print(True)
else:
    print(False)
