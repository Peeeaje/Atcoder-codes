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

if N == 1:
    print("No")
    quit()

sum_ = A[-1]
r = 0
ans = 0
for l in range(N):
    sum_ -= A[l-1]

    if r < l:
        r = l
        sum_ = 0 # sumの場合は0にする

    while r <= N - 1 and sum_ + A[r] < s * 0.1:
        sum_ += A[r]
        r += 1

    if sum_ + A[r] == s * 0.1:
        print("Yes")
        quit()
    
print("No")