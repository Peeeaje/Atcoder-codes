n = int(input())

# dp[i][j]: i番目の料理を食べた後に状態がjであるときの、最大の幸福度
dp = [[0] * 2 for _ in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    if i == 0:
        if x == 0:
            dp[i][0] = max(0, y)
        else:
            dp[i][1] = max(0, y)
        continue

    if x == 0:
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] + y, dp[i - 1][1] + y)
        dp[i][1] = dp[i - 1][1]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = max(dp[i - 1][0] + y, dp[i - 1][1])
print(max(dp[-1]))