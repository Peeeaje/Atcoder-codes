import math

N = int(input())

ans = set()
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        ans.add(i)
        ans.add(N // i)
for a in ans:
    print(a)
