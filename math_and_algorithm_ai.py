import numpy as np

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A_cumsum = np.cumsum(A)


def get_sum(l, r):
    if l == 1:
        return A_cumsum[r - 1]
    else:
        return A_cumsum[r - 1] - A_cumsum[l - 2]


for i in range(Q):
    L, R = map(int, input().split())
    print(get_sum(L, R))
