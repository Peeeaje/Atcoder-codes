import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, M = map(int, readline().split())
ps = list()
for i in range(M):
    temp = input().split()
    ps.append(temp)

WA = [0] * N
AC = [0] * N
WA_int = 0
for p_s in ps:
    p_s[0] = int(p_s[0]) - 1

    if p_s[1] == "WA" and AC[p_s[0]] == 0:
        WA[p_s[0]] += 1
    if p_s[1] == "AC" and AC[p_s[0]] == 0:
        AC[p_s[0]] += 1
        WA_int += WA[p_s[0]]
print(sum(AC), WA_int)