import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

N, K = map(int, read().split())


def g1(x: int):
    list_temp = sorted(list(str(x)), reverse=True)
    return int("".join(list_temp))


def g2(x: int):
    list_temp = sorted(list(str(x)), reverse=False)
    return int("".join(list_temp))


def main(x: int):
    return g1(x) - g2(x)


ans = N
for i in range(K):
    ans = main(ans)
print(ans)