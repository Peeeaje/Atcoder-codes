import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, K = from_readline()
A = from_readline()
B = from_readline()

if np.sum(np.abs(A-B)) - K <= 0 and (np.sum(np.abs(A-B)) - K) % 2 == 0:
    print("Yes")
else:
    print("No")