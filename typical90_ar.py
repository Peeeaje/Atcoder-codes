import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, Q = map(int, input().split())
A = list(map(int, input().split()))

temp = 0

for i in range(Q):
    t = list(map(int, input().split()))

    if t[0] == 2:
        temp += 1

    elif t[0] == 1:
        A[(t[1] - temp - 1) % N], A[(t[2] - temp - 1) % N] = (
            A[(t[2] - temp - 1) % N],
            A[(t[1] - temp - 1) % N],
        )

    else:
        print(A[(t[1] - temp - 1) % N])
