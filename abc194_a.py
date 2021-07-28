import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


A, B = map(int, read().split())

if A + B >= 15 and B >= 8:
    ans = 1
elif A + B >= 10 and B >= 3:
    ans = 2
elif A + B >= 3:
    ans = 3
else:
    ans = 4

print(ans)