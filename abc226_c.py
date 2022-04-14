import sys

sys.setrecursionlimit(300000)


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].append(v)


N = int(input())
G = Graph(N)

A = []
T = []
K = []
for i in range(N):
    TKA = list(map(int, input().split()))
    T.append(TKA[0])
    K.append(TKA[1])
    A = TKA[2:]

    for a in A:
        G.add_edge(i, a - 1)


seen = [0] * N


def dfs(G, v):
    seen[v] = True

    for next_v in G.edges[v]:
        if seen[next_v] == 1:
            continue
        dfs(G, next_v)


dfs(G, N - 1)
time = 0
for i in range(len(seen)):
    b = seen[i]
    if b:
        time += T[i]
print(time)
