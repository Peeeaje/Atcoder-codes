N, W = map(int, input().split())
dp = [[-float('inf')] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w, v = map(int, input().split())
    for j in range(W + 1):
        if j - w < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(max(dp[-1]))