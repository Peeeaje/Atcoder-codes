N, W = map(int, input().split())
MAX = 100000 + 1
dp = [[float('inf')] * MAX for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w, v = map(int, input().split())
    for j in range(MAX):
        if j - v < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v] + w)

ans = 0
for i in range(MAX):
    if dp[-1][i] != -float('inf') and dp[-1][i] <= W:
        ans = i
print(ans)