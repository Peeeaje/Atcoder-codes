from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)

ans = []
for i in range(3 * n):
    d[a[i]] += 1
    if d[a[i]] == 2:
        ans.append(a[i])

print(*ans)
