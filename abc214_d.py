import heapq
import math
import sys
from heapq import heappop, heappush

import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


n = int(input())
g = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])
g = [np.array(i) for i in g]
g = np.array(g)
print(g)

temp = -1
node = -1

for i in range(len(g)):
    if len(g[i]) > temp:
        temp = len(g[i])
        node = i

import sys

sys.setrecursionlimit(300000)

seen = [0] * (n + 1)
v = node

temp = [10**9] * n
temp[node] = 0


def dfs(G, v):
    seen[v] = True
    for next_v in G[v]:
        next_v = next_v[0]
        if seen[next_v] == 1:
            continue
        print(G[v])
        print(G[v][:, 0])
        temp[next_v] = temp[v] + G[v][1][G[v][:, 0] == next_v]
        dfs(G, next_v)


dfs(g, node)
print(temp)
