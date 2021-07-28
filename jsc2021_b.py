import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, M = map(int, readline().split())
A = readline().decode().split()
B = readline().decode().split()

ans = list()

for i in A:
    if i not in B:
        ans.append(i)

for i in B:
    if i not in A:
        ans.append(i)

ans = list(set(ans))
ans.sort()
print(" ".join(ans))