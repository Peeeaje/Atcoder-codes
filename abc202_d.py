import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decod(e(), dtype=dtype, sep=" "))


A, B, K = from_read()

n = A + B
n_pattern = np.int64(2 ** (A + B))
ans = str()

btm = np.int64(-1)
up = n_pattern - 1

for i in range(n):
    print(btm, up)
    if K >= (btm + up) / 2:
        btm = (btm + up) // 2
        ans += "A"
    else:
        up = (btm + up) // 2
        ans += "B"

print(ans)
