# Find the largest palindrome less than a given number that is a multiple of
# two 3 digit numbers.

def next_pal(n):
    # Get the next palindrome less than n < 1000000
    # n is 6 digits
    # Divide by 1000
    # Subtract 1, reverse and concatenate
    p = n//1000
    p -= 1
    return p*1000 + int(str(p)[::-1])

t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    if n < 101101 and n >= 1000000:
        continue
