x, y, z = map(int, input().split())
S = input()

# dp[i][j]: Capslockがon(j=1), off(j=0)で終わる場合で、i文字目まで入力するのに必要な最小時間
dp = [[0] * 2 for _ in range(len(S))]
dp[0][0] = x if S[0] == "a" else y
dp[0][1] = y + z if S[0] == "a" else x + z

for i in range(1, len(S)):
    if S[i] == "A":
        dp[i][0] = min(dp[i - 1][0] + y, dp[i - 1][1] + z + y)
        dp[i][1] = min(dp[i - 1][1] + x, dp[i - 1][0] + z + x)
    else:
        dp[i][0] = min(dp[i - 1][0] + x, dp[i - 1][1] + z + x)
        dp[i][1] = min(dp[i - 1][1] + y, dp[i - 1][0] + z + y)

print(min(dp[-1]))