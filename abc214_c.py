N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N
dp[0] = min(B[0], B[-1]+ A[-1])

for i in range(1,2*N):
    i = i%N
    dp[i] = min(dp[i-1] + A[i-1], B[i])

for i in dp:
    print(i)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = B.index(min(B))

dp = [0] * N
dp[s] = B[s]

for i in range(s, N+s):
    i = i % N
    dp[i] = min(dp[i-1] + A[i-1], B[i])

for i in dp:
    print(i)