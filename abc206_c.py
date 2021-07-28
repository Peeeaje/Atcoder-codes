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

ans = N * (N - 1) // 2
c = collections.Counter(A)
temp = [c[a] for a in c if c[a] >= 2]
temp = sum([a * (a - 1) // 2 for a in temp])
print(ans - temp)
