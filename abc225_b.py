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


N = from_readline()[0]
AB = from_read()  # .reshape(-1, 2)

for a, b in collections.Counter(AB).most_common():
    if b == N - 1 or b == 1:
        pass
    else:
        print("No")
        exit()
print("Yes")
