import sys
import numpy as np
import math
import collections

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = int(readline())
A = from_readline()

C = collections.Counter(A).most_common()
print(C)

for i in range(len(A)):
    temp = [[items[0], items[1]] for items in C]
    ind = [items[0] for items in temp if items[0] == A[i]][0] - 1
    temp[temp == ind][1] -= 1
    print(ind)
    print(temp)