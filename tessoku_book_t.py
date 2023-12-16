s = list(input())
t = list(input())
n_s = len(s)
n_t = len(t)

dp = [[0] * (n_t + 1) for _ in range(n_s + 1)]

for i in range(1, n_s + 1):
    for j in range(1, n_t + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if s[i - 1] == t[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

print(dp[n_s][n_t])
