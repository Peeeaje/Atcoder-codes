import math

N = int(input())

s = []
for i in range(2, int(math.sqrt(N)) + 1):
    while N % i == 0:
        s.append(i)
        N //= i

if (N != 0) and (N != 1):
    s.append(N)

print(" ".join(map(str, s)))
