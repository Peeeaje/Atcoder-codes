import numpy as np

D = int(input())
N = int(input())
l = np.array([0] * (D + 1))
for i in range(N):
    L, R = map(int, input().split())
    l[L : R + 1] += 1

for v in l[1:]:
    print(v)
