N, M = map(int, input().split())


class Graph:
    def __init__(self, n):
        """
        n: 頂点数
        """
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v):
        """
        uからvへの辺を追加する
        """
        self.edges[u].append(v)

    def get_edges(self, u):
        """
        uから出ている辺を返す
        """
        return self.edges[u]


g = Graph(N)
for i in range(M):
    a, b = map(int, input().split())
    g.add_edge(a - 1, b - 1)

import sys

sys.setrecursionlimit(300000)


def dfs(G, v, seen):
    seen[v] = True

    for next_v in G.edges[v]:
        if seen[next_v] == 1:
            continue
        dfs(G, next_v, seen)


seen = [0] * (N + 1)

ans = []
for i in range(N):
    dfs(g, i, seen)
    ans.extend(seen)

print(sum(ans))
