import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


KEY = input()
ans = 0
for i in range(10000, 20000):
    temp = str(i)[1:]
    for j in range(10):
        if (KEY[j] == "o" and str(j) not in temp) or (KEY[j] == "x" and str(j) in temp):
            break
        elif j == 9:
            ans += 1

print(ans)