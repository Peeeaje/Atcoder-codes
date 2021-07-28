import sys
import numpy as np

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
max_A = max(A)
min_B = min(B)
if min_B - max_A + 1 >= 1:
    print(min_B - max_A + 1)
else:
    print(0)