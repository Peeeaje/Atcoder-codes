import sys
import numpy as np
import collections

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(input())
A = [i % 46 for i in list(map(int, input().split()))]
B = [i % 46 for i in list(map(int, input().split()))]
C = [i % 46 for i in list(map(int, input().split()))]

C_A = collections.Counter(A)
C_B = collections.Counter(B)
C_C = collections.Counter(C)

ans = 0

for i in range(0, 47):
    for j in range(0, 47):
        for k in range(0, 47):
            if (i + j + k) % 46 == 0:
                ans += C_A[i] * C_B[j] * C_C[k]

print(ans)