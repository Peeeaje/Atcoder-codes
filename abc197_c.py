import sys
import numpy as np
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = int(readline())
A = from_readline()

for i in range(2 ** (N - 1)):
    temp = N + 1
    ans = list()
    for j in range(N):
        if (i >> j) & 1:
            pass
    ans.append(A[0:temp])
    print(bin(i))
    print(ans)
