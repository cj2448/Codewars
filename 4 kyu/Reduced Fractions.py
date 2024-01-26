import math

n = 500000003
count = 0

for i in range(1, n):
    if  math.gcd(i, n) == 1:
        count += 1

print(count)