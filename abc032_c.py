import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, K = from_readline()
s = from_read()

r = 0
ans = 0

if 0 in s:
    print(N)
    quit()

prod = s[-1]
r = 0
ans = 0
for l in range(N):
    prod //= s[l-1]

    if r < l:
        r = l
        prod = 1 # sumの場合は0にする

    while r <= N - 1 and prod * s[r] <= K:
        prod *= s[r]
        r += 1

    ans = max(ans, r-l)
    
print(ans)