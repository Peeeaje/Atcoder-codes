import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, L = from_read()
dp = np.zeros(N+1, dtype=np.int64)
dp[0] = 1

for i in range(1, N+1):
    if i < L:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[i-L])% (10**9 + 7)
print(dp[N])