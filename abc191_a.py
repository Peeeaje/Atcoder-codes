import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

V, T, S, D = map(int, read().split())
if V * T <= D <= V * S:
    print("No")
else:
    print("Yes")
