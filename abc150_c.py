import sys
import numpy as np
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = int(readline())
P = tuple(list(map(int, readline().split())))
Q = tuple(list(map(int, readline().split())))

n = 0
for i in itertools.permutations(range(1, N + 1)):
    n += 1
    if P == i:
        a = n
    if Q == i:
        b = n
print(abs(a - b))
