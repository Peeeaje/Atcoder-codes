import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

N, M = map(int, readline().split())
AB = list()

for i in range(M):
    temp = list(map(int, readline().split()))
    AB.append(temp)

K = int(readline())
CD = list()

for i in range(K):
    temp = list(map(int, readline().split()))
    CD.append(temp)

ans = 0
for i in range(2 ** K):
    temp_ans = 0
    ans_set = set()
    for j in range(K):
        if (i >> j) & 1:
            ans_set.add(CD[j][1])
        else:
            ans_set.add(CD[j][0])

    for k in range(M):
        if AB[k][0] in ans_set and AB[k][1] in ans_set:
            temp_ans += 1

    ans = max(ans, temp_ans)

print(ans)
