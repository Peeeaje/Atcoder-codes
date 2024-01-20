n = int(input())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    d[a[i]] = i + 1

ans = []
tmp = -1
for i in range(n):
    ans.append(d[tmp])
    tmp = d[tmp]
print(*ans)
