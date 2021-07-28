import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, X = map(int, readline().split())
A = list(map(int, readline().split()))
A = [str(x) for x in A if x != X]
s = " ".join(A)
print(s)