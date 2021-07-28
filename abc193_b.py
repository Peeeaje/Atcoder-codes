import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

N = int(readline())
APX = np.array(list(map(int, read().split()))).reshape(N, 3)

ans = 100000000000
for i in range(N):
    if (APX[i][2] - APX[i][0]) >= 1:
        ans = min(ans, APX[i][1])

print(-1 if ans == 100000000000 else ans)