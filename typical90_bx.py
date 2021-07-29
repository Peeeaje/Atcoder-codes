import sys
import numpy as np
from bisect import bisect_left

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = int(input())
A = list(map(int, input().split()))
s = sum(A)
A = *A, *A


A = np.cumsum(A)
r = 0

if N == 1:
    print("No")
else:
    for l in range(N):
        while (A[r] - A[l]) * 10 < s:
            r += 1

        if (A[r] - A[l]) * 10 == s:
            print("Yes")
            quit()
        
    print("No")