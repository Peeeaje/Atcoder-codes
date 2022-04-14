import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
ans = 0
for a in set(A):
    if a == 50000:
        ans += c[100000 - a] * (c[a] - 1) / 2
    else:
        ans += c[100000 - a] * c[a] / 2
print(int(ans))
