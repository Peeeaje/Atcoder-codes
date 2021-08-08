import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")



H, W, N = from_readline()
AB = from_read().reshape(N,2)
A = list(AB[:, 0])
B = list(AB[:, 1])

A_sort = np.sort(list(set(A)))
nums_a = [i+1 for i in range(len(A_sort))]
A_dict = dict(zip(A_sort, nums_a))

B_sort = np.sort(list(set(B)))
nums_b = [i+1 for i in range(len(B_sort))]
B_dict = dict(zip(B_sort, nums_b))

A = [A_dict[a] for a in A]
B = [B_dict[b] for b in B]

for i in zip(A, B):
    print(*i)