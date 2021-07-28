import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

A, B = map(int, read().split())
print(100 - (B * 100) / A)
