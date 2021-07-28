import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

H, W = map(int, readline().split())
A = list(map(int, read().split()))
m = min(A)
ans = 0
for i in range(H * W):
    if A[i] > m:
        ans += A[i] - m
print(ans)