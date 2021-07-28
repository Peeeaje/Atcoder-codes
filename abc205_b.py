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


N = from_readline()
A = sorted(from_readline())

B = np.ones(N)
B = np.cumsum(B)
if all(A == B):
    print("Yes")
else:
    print("No")