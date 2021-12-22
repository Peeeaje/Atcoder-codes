import math


def enumerate_divisor(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i


K = int(input())
ans = 0
for i in enumerate_divisor(K):
    for j in enumerate_divisor(K // i):
        if j < i:
            continue
        ans += 1
print(ans)
