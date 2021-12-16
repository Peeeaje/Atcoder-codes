import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = from_readline()[0]
A = from_readline()
X = from_readline()[0]
A_cumsum = np.cumsum(A)

sum_A = np.sum(A)
syou = X // sum_A
amari = X % sum_A

temp = np.where(A_cumsum > amari)
print(syou * N + temp[0][0] + 1)