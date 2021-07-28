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
CP = np.array([], dtype=np.int64)
for i in range(N):
    CP = np.append(CP, from_readline())
CP = CP.reshape(N, 2)
Q = from_readline()[0]
LR = from_read().reshape(Q, 2)

cumsum_1 = np.cumsum([a[1] if a[0] == 1 else 0 for a in CP])
cumsum_2 = np.cumsum([a[1] if a[0] == 2 else 0 for a in CP])
cumsum_1 = np.append(cumsum_1, 0)
cumsum_2 = np.append(cumsum_2, 0)

for i in LR:
    L = i[1] - 1
    R = i[0] - 2
    ans_1 = cumsum_1[L] - cumsum_1[R]
    ans_2 = cumsum_2[L] - cumsum_2[R]
    print(ans_1, ans_2)