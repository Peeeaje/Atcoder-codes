N, X = map(int, input().split())
dp = [set([]) for i in range(N + 1)]
dp[0].add(0)

for i in range(1, N + 1):
    a, b = map(int, input().split())
    for n in dp[i - 1]:
        if n <= X:
            dp[i].add(n + a)
            dp[i].add(n + b)


if X in dp[N]:
    print("Yes")
else:
    print("No")
