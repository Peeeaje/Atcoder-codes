n = int(input())
MAX = 1502

f = [[0] * MAX for _ in range(MAX)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    f[a][b] += 1
    f[a][d] -= 1
    f[c][b] -= 1
    f[c][d] += 1

for i in range(MAX):
    for j in range(1, MAX):
        f[i][j] += f[i][j - 1]

ans = 0
for i in range(0, MAX):
    for j in range(MAX):
        f[i][j] += f[i - 1][j]
        if f[i][j] > 0:
            ans += 1

print(ans)