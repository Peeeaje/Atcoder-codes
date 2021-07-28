import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = from_readline()[0]
A = np.sort(from_readline())
Q = from_readline()[0]
B = from_read()

ans = []


i = B[0]

from bisect import bisect_left

for i in B:
    arr = A
    left = bisect_left(arr, i)

    if left == 0:
        print(abs(A[0] - i))
    elif left == N:
        print(abs(A[N - 1] - i))

    else:
        print(min(abs(A[left] - i), abs(A[left - 1] - i)))
