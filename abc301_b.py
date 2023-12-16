n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n - 1):
    f = a[i]
    t = a[i + 1]
    if f < t:
        d = 1
    else:
        d = -1
    ans.extend(list(range(f, t, d)))

ans.append(a[-1])
print(*ans)
