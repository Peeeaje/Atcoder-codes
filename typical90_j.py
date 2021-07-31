import numpy as np

N = int(input())
C1 = [0]
C2 = [0]

for i in range(N):
    C, P = map(int, input().split())

    if C == 1:
        C1.append(P)
        C2.append(0)
    else:
        C1.append(0)
        C2.append(P)

C1 = np.cumsum(C1)
C2 = np.cumsum(C2)
Q = int(input())

for i in range(Q):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1

    print(C1[r + 1] - C1[l], C2[r + 1] - C2[l])