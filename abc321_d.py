import bisect

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))
cumsum_b = [0] * (m + 1)
for i in range(m):
    cumsum_b[i + 1] = cumsum_b[i] + b[i]

total = 0
for v in a:
    index = bisect.bisect_left(b, p - v)
    total += p * (m - index)
    total += v * index + cumsum_b[index]

print(total)
# 7, 7, 9, 11