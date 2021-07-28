import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
ans = "Takahashi"

A, B, C = map(int, read().split())
if (C == 0 and A <= B) or (C == 1 and A < B):
    ans = "Aoki"

print(ans)