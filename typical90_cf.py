import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    from itertools import groupby
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


N = int(input())
S = input()

pos_combi = N * (N - 1) // 2
continuous_combi = 0

for _, i in runLengthEncode(S):
    continuous_combi += i * (i - 1) // 2
    
print(pos_combi - continuous_combi)