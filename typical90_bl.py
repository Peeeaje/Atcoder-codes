import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, Q = from_readline()
A = from_readline()
diff = np.insert(np.append(np.diff(A), 0), 0, 0)

for i in range(Q):
    L, R, V = from_readline()
    diff[L-1] = diff[L-1] + V
    diff[R] = diff[R] - V
    ans = 0
    for i in range(len(diff[1:-1])):
        ans += abs(diff[i+1])
    print(ans)

