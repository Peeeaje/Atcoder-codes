n, d = map(int, input().split())
S = [input() for _ in range(n)]

ans = 0
tmp = 0
for i in range(d):
    if all([s[i] == "o" for s in S]):
        tmp += 1
    else:
        tmp = 0
    ans = max(ans, tmp)

print(ans)
