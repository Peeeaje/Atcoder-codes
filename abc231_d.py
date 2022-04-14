import sys
import numpy as np
import collections

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, M = from_readline()
AB = from_read()
c = collections.Counter(AB).most_common()
print("No" if c[0][1] > 2 else "Yes")

