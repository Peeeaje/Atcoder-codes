import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

N, S, D = map(int, readline().split())
XY = np.array(list(map(int, read().split()))).reshape(N, 2)

for i in range(N):
    if XY[i][0] < S and XY[i][1] > D:
        print("Yes")
        exit()
print("No")
