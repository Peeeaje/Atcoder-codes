s = list(input())
t = list(input())
n_s = len(s)
n_t = len(t)

dp = [[0] * (n_t + 1) for _ in range(n_s + 1)]
dp[0] = [i for i in range(n_t + 1)]
for i in range(n_s + 1):
    dp[i][0] = i

for i in range(1, n_s + 1):
    for j in range(1, n_t + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

print(dp[n_s][n_t])