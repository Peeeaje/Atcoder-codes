import sys
import numpy as np
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, K = from_readline()


AB = from_read().reshape(N, 2)
A = AB[:, 0] - AB[:, 1]
B = AB[:, 1]
AB = np.sort(np.hstack([A, B]))

print(np.sum(AB[-K:]))