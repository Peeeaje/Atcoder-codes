n, m = map(int, input().split())
c = list(input().split())

d = list(input().split())
p = list(map(int, input().split()))
d = dict(zip(["OTHER"] + d, p))

ans = 0
for i in range(n):
    ans += d.get(c[i], d["OTHER"])

print(ans)
