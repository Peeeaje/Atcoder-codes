import math

N, L = map(int, input().split())

ans = 0
dp = [0] * (N+1)
dp[0] = 1
for i in range(1, N+1):
    if i == 0:
        dp[i] = 1 
    else:
        if i >= L:
            dp[i] = dp[i-1] + dp[i-L]
        else:
            dp[i] = dp[i-1]
print(dp[-1]%(10 ** 9 + 7))

