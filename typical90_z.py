import sys

sys.setrecursionlimit(300000)


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)


def dfs(G, v, color):
    colors[v] = color
    seen[v] = True

    for next_v in G.edges[v]:

        if seen[next_v] == 1:
            continue
        dfs(G, next_v, 1 - color)


N = int(input())
G = Graph(N + 1)
colors = [-1] * (N + 1)


for i in range(N - 1):
    A, B = map(int, input().split())
    G.add_edge(A, B)

seen = [0] * (N + 1)
dfs(G, 1, 0)
if sum([1 for i in colors if i == 0]) > sum([1 for i in colors if i == 1]):
    print(" ".join([str(i) for i in range(len(colors)) if colors[i] == 0][: N // 2]))
else:
    print(" ".join([str(i) for i in range(len(colors)) if colors[i] == 1][: N // 2]))
