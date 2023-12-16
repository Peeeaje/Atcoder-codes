n = int(input())
pa = []
for i in range(n):
    p, a = map(int, input().split())
    pa.append((p, a))

dp = [[0] * (n + 2) for _ in range(n + 2)]

ans = -1
for i in range(1, n + 1):
    for l in range(1, i + 1):
        r = l + n - i

        if l == 1:
            left_point = 0
        else:
            left_point = pa[l - 2][1] if l <= pa[l - 2][0] <= r else 0

        if r == n:
            right_point = 0
        else:
            right_point = pa[r][1] if l <= pa[r][0] <= r else 0

        dp[l][r] = max(dp[l - 1][r] + left_point, dp[l][r + 1] + right_point)
        ans = max(ans, dp[l][r])

print(ans)