import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline


def judge(x: int):
    ten = list(map(int, str(x)))
    eight = list(map(int, str(oct(x)[2:])))
    jud = ten + eight
    if 7 not in jud:
        return True
    else:
        return False


N = int(read())
ans = 0
for i in range(1, N + 1):
    if judge(i):
        ans += 1
print(ans)