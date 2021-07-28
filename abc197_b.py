import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


H, W, X, Y = map(int, readline().split())
S = list()
for i in range(H):
    S.append(input())
ans = 1
X -= 1
Y -= 1

i = 1
while Y - i >= 0 and S[X][Y - i] == ".":
    ans += 1
    i += 1
i = 1
while Y + i < W and S[X][Y + i] == ".":
    ans += 1
    i += 1
i = 1
while X - i >= 0 and S[X - i][Y] == ".":
    ans += 1
    i += 1
i = 1
while X + i < H and S[X + i][Y] == ".":
    ans += 1
    i += 1

print(ans)
