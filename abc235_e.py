import copy
import bisect


N, M, Q = map(int, input().split())


class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]


weight_node = []


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)


def kruskal(G, weight_node):
    unionfind = UnionFind(N)
    ans = []
    for node in weight_node:
        u, v = node[1], node[2]
        if not unionfind.is_same(u, v):
            if len(node) == 4:
                ans.append(node[3])
            else:
                unionfind.union(u, v)
            # ans.append(node)
    return ans


G = Graph(N)
for i in range(M):
    a, b, c = map(int, input().split())
    G.add_edge(a - 1, b - 1)
    weight_node.append((c, a - 1, b - 1))

for i in range(Q):
    u, v, w = map(int, input().split())
    weight_node.append((w, u - 1, v - 1, i))

weight_node = sorted(weight_node, reverse=False, key=lambda x: x[0])
temp = set(kruskal(G, weight_node))
for i in range(Q):
    if i in temp:
        print("Yes")
    else:
        print("No")
