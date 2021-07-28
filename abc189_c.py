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
A = from_read()

ans = 0
for l in range(N):
    mini = A[l]
    for r in range(l, N):
        mini = min(mini, A[r])
        ans = max(ans, mini * (r - l + 1))
print(ans)
