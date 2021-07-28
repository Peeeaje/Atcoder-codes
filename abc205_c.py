import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


A, B, C = from_read()

if C % 2 == 0:
    A, B = abs(A), abs(B)
    if A == B:
        print("=")
    elif A > B:
        print(">")
    else:
        print("<")
else:
    if (A < 0 and B > 0) or (A > 0 and B < 0):
        if A > B:
            print(">")
        else:
            print("<")

    elif A >= 0 and B >= 0:
        if A == B:
            print("=")
        elif A > B:
            print(">")
        else:
            print("<")

    else:
        if A == B:
            print("=")
        elif A > B:
            print(">")
        else:
            print("<")
