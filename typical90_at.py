import sys
import numpy as np
from collections import Counter

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = from_readline()[0]
A = Counter(from_readline() % 46)
B = Counter(from_readline() % 46)
C = Counter(from_readline() % 46)

ans = 0

for i in range(46):
    for j in range(46):
        for k in range(46):

            if (i + j + k) % 46 == 0:
                ans += A[i] * B[j] * C[k]

print(ans)