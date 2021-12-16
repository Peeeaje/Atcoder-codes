import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


def can_div_by_2(array: np.array):
    return np.all(array % 2 == 0)


A = from_read()[1:]
ans = 0

while can_div_by_2(A):
    ans += 1
    A = A // 2

print(ans)
