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


N, P, Q = from_readline()
A = from_readline()
ans = 0
for i in itertools.combinations(A, 5):
    if np.prod(i)%P == Q:
        ans +=1
print(ans)