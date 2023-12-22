
MOD = 998244353
n, m, k = map(int, input().split())
edges = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

# dp[i][j]: A_0からi回移動を行った際に、jの都市にいるパターン数
dp = [[0] * n for _ in range(k + 1)]
dp[0][0] = 1
for i in range(1, k + 1):
    tmp = sum(dp[i - 1])
    for j in range(n):
        # dp[i][j] = sum(dp[i - 1][k] for k in {all_edges - edges[j]})
        # dp[i][j] = sum(dp[i - 1][k] for k in {all_edges}) - sum(dp[i - 1][k] for k in {edges[j]})
        dp[i][j] = (tmp - dp[i - 1][j]) % MOD
        for k in edges[j]:
            dp[i][j] -= dp[i - 1][k] % MOD
        dp[i][j] %= MOD

print(dp[i][0] % MOD)
