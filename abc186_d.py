import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = from_readline()[0]
A = np.sort(from_read())

ans = 0
A_csum = np.cumsum(A)

# while len(A):
#     temp = A - A[-1]
#     ans += np.sum(temp)
#     A = A[:-1]
for i in range(N):
    ans += (A_csum[-1] - A_csum[i]) - A[i] * (N - i - 1)
print(ans)