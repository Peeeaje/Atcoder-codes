import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


x, y = map(int, input().split())
if x == y:
    print(x)
else:
    list = [0, 1, 2]
    list.remove(x)
    list.remove(y)

    print(list[0])
