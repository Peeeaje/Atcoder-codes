import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


A, B, C = from_read()
if A % C == 0:
    n = A
else:
    n = (A // C + 1) * C

if A <= n <= B:
    print(n)
else:
    print(-1)
