import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

N = int(readline())
xy = np.array(list(map(int, read().split()))).reshape(N, 2)
ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if -1 <= ((xy[i][1] - xy[j][1]) / (xy[i][0] - xy[j][0])) <= 1:
            ans += 1

print(ans)