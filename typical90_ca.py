import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")

H, W = from_readline()
AB = from_read().reshape(-1, W)
A = AB[:H, :]
B = AB[H:, :]

ans = 0
for y in range(H-1):
    for x in range(W-1):
        Axy = A[y,x]
        Bxy = B[y,x]

        diff = Axy - Bxy
        ans += abs(diff)
        A[y:y+2, x:x+2] -= diff


if np.array_equal(A, B):
    print("Yes")
    print(ans)
else:
    print("No")