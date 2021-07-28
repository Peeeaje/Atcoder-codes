import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


A, B, C = from_read()
gcd_ABC = math.gcd(math.gcd(A, B), math.gcd(B, C))
print(A // gcd_ABC + B // gcd_ABC + C // gcd_ABC - 3)
