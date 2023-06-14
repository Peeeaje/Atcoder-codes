import numpy as np

H, W = map(int, input().split())
X = []
for i in range(H):
    X.append(list(map(int, input().split())))
X = np.array(X)
X = np.cumsum(X, axis=1)
X = np.cumsum(X, axis=0)
Q = int(input())


def get_sum(X, A, B, C, D):
    if A == 1 and B == 1:
        return X[C - 1, D - 1]
    elif A == 1:
        return X[C - 1, D - 1] - X[C - 1, B - 2]
    elif B == 1:
        return X[C - 1, D - 1] - X[A - 2, D - 1]

    return X[C - 1, D - 1] - X[C - 1, B - 2] - X[A - 2, D - 1] + X[A - 2, B - 2]


for i in range(Q):
    A, B, C, D = map(int, input().split())
    n = X[C - 1, D - 1] - X[C - 1, B - 2] - X[A - 2, D - 1] + X[A - 2, B - 2]
    print(get_sum(X, A, B, C, D))
