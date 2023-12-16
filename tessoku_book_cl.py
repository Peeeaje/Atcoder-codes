n, k = map(int, input().split())
a = list(map(int, input().split()))
sa = [0]
for i in range(n):
    sa.append(sa[-1] + a[i])

l = 0
r = 1
ans = 0

while l <= n:
    while r <= n and sa[r] - sa[l] <= k:
        r += 1
    r -= 1
    ans += r - l
    l += 1

print(ans)