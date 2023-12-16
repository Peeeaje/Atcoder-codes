import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.color = [-1] * n

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def dfs(self, v):
        for u in self.edges[v]:
            if self.color[u] == -1:
                self.color[u] = 1 - self.color[v]
                if not self.dfs(u):
                    return False
            elif self.color[u] == self.color[v]:
                return False
        return True

    def bipartite(self):
        bipartite = True
        for i in range(self.n):
            if self.color[i] == -1:
                self.color[i] = 0
                bipartite &= self.dfs(i)
        return bipartite


g = Graph(N)
for a, b in zip(A, B):
    a -= 1
    b -= 1
    g.add_edge(a, b)

if g.bipartite():
    print("Yes")
else:
    print("No")
