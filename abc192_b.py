import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = input()
O = S[::2]
E = S[1::2]
if len(S) == 1:
    E = "D"
if O.islower() and E.isupper():
    print("Yes")
else:
    print("No")
