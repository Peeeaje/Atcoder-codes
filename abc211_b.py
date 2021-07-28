import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


l = list()
for i in range(4):
    l.append(input())

if ("H" not in l or "2B" not in l or "3B" not in l or "HR" not in l):
    print("No")
else:
    print("Yes")