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
sc = list()
for i in range(M):
    temp = tuple(map(int, readline().split()))
    sc.append(temp)
sc = set(tuple(sc))


def main(N, M, sc):
    ans = ["0"] * N
    for i in sc:
        if ans[i[0] - 1] != "0" or (i[0] == 1 and i[1] == 0 and N >= 2):
            print(-1)
            exit()
        ans[i[0] - 1] = str(i[1])

    if ans[0] == "0" and N >= 2:
        ans[0] = "1"
    print("".join(ans))


main(N, M, sc)