import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

N = int(read())
x = list()

for i in range(2, int(N ** 0.5) + 1):
    temp = i ** 2
    while temp <= N:
        x.append(temp)
        temp *= i
x = set(x)
print(N - len(x))