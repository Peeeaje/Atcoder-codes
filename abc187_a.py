import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

A, B = read().decode().split()
A = int(A[0]) + int(A[1]) + int(A[2])
B = int(B[0]) + int(B[1]) + int(B[2])
print(A if A > B else B)
