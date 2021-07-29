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
XY = from_read().reshape(N,2)
X = np.sort(XY[:,0])
Y = np.sort(XY[:,1])
ansX = np.sum(np.abs(X - np.median(X)))
ansY = np.sum(np.abs(Y - np.median(Y)))
print(int(ansX + ansY))