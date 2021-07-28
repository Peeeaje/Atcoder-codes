import sys
import numpy as np
import collections

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = from_readline()[0]
A = from_readline()
B = from_readline()
C = from_readline()

BC = [B[C[i] - 1] for i in range(N)]

A_C = collections.Counter(A)
BC_C = collections.Counter(BC)

ans = 0

for i in range(N + 1):
    ans += A_C[i] * BC_C[i]

print(ans)
