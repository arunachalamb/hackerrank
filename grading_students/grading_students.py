import sys

def solve(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            d = grades[i]//5
            r = grades[i]%5
            if r > 2:
                grades[i] = (d + 1)*5


n = int(input().strip())
grades = []
for i in range(n):
   grades.append(int(input().strip()))
solve(grades)
print ("\n".join(map(str, grades)))
