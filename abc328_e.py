N, M, K = map(int, input().split())
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.weights = [[float('inf')] * n for _ in range(n)]

    def add_edge(self, u, v, w):
        self.edges[u].append(v)
        self.edges[v].append(u)
        self.weights[u][v] = w
        self.weights[v][u] = w

G = Graph(N)
edges = []
weights = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G.add_edge(u - 1, v - 1, w)
    edges.append((u - 1, v - 1))
    weights[u - 1][v - 1] = w % K
    weights[v - 1][u - 1] = w % K

ans = float('inf')
import itertools

for nodes in itertools.combinations(range(M), N - 1):
    uf = UnionFind(N)
    cost = 0
    f = True
    for i in nodes:
        u, v = edges[i]
        cost += weights[u][v]
        cost %= K
        if uf.same(u, v):
            f = False
            break
        uf.union(u, v)

    if uf.group_count() == 1 and f:
        ans = min(ans, cost % K)

print(ans)