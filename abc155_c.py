import sys
from typing import Collection
import numpy as np
import collections

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = int(readline())
S = read().decode().split()


def main(N, S):
    C = collections.Counter(S).most_common()
    values, counts = zip(*C)
    max_counts = max(counts)
    C = sorted([item[0] for item in C if item[1] == max_counts])
    for c in C:
        print(c)


main(N, S)