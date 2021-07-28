import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")

S = input()


dict = {"c":1, "h":2, "o":3, "k":4, "u":5,"d":6, "a":7, "i":8}
s = set(["c", "h", "o", "k", "u","d", "a", "i"])
l = [0 for i in range(9)]
l[0] = 1
for i in S:
    if i not in s:
        pass
    else:
        l[dict[i]] += (l[dict[i]-1]%(10**9+7))
l[-1] = l[-1]%(10**9+7)
print(l[-1])