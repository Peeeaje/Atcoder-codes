import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, M = from_readline()
V = np.array([0 for i in range(N+1)])

for i in range(M):
    a, b = from_readline()
    if b < a:
        V[a] += 1
    if a < b:
        V[b] += 1

print(sum(V==1))