import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

ans = -1
N, X = map(int, readline().split())
VP = np.array(list(map(int, read().split()))).reshape(N, 2)
V = VP[:, 0]
P = VP[:, 1]
VP = [a * b for a, b in zip(V, P)]
VP = list(np.cumsum(VP))


for i in range(N):
    if VP[i] > X * 100:
        print(i + 1)
        exit()
print(-1)