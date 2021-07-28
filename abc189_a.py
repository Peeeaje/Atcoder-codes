import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

C = read().decode().rstrip()
print("Won" if len(set(C)) == 1 else "Lost")
