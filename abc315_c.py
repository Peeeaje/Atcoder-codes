n = int(input())
l = []
for _ in range(n):
    f, t = map(int, input().split())
    l.append((f, t))

l.sort(key=lambda x: -x[1])

a = l[0]

ans = -1
for i in range(1, n):
    b = l[i]
    if a[0] == b[0]:
        tmp = a[1] + b[1] // 2
    else:
        tmp = a[1] + b[1]
    ans = max(ans, tmp)

print(ans)