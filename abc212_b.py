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

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

f1 = 0
f2 = 0
for i in range(len(S)-1):
    s = S[i]
    s1 = S[i+1]

    if int(s1) == l[int(s)+1]:
        f1 += 1
    if s == s1:
        f2 += 1

if f1 == 3 or f2 == 3:
    print("Weak")
else:
    print("Strong")