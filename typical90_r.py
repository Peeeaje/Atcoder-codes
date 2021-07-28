import sys
import math
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


T = from_readline()[0]
L, X, Y = from_readline()
Q = from_readline()[0]
E = from_read()

# y ** 2 + (z - L//2) ** 2 == (L // 2) ** 2
for i in range(Q):
    thi = 2 * math.pi * E[i] / T  # thiはradian
    y = -1 * math.sin(thi) * (L / 2)
    z = L / 2 - (math.cos(thi) * (L / 2))

    leng = math.sqrt(X ** 2 + (y - Y) ** 2 + z ** 2)
    sin_ans = z / leng
    print(math.degrees(math.asin(sin_ans)))
