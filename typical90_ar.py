import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, Q = from_readline()
A = from_readline()


shift = 0
for i in range(Q):
    T, x, y = from_readline()
    if T == 1:
        A[x-1], A[y-1] = A[y-1], A[x-1]
    if T == 2:
        shift += 1
    else:
        print(A[x - shift])