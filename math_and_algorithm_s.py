import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

ans = 0
for i in range(1, 4):
    ans += c[i] * (c[i] - 1) // 2
print(ans)
