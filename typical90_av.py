import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, K = from_readline()
A = list()
B = list()
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A = np.array(A)
B = np.array(B)
A = A - B
C = np.hstack([A, B])
C = np.sort(C)
print(np.sum(C[-K:]))
