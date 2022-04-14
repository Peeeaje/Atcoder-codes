class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)


N, Q = map(int, input().split())
X = list(map(int, input().split()))
G = Graph(N)

for i in range(N - 1):
    a, b = map(int, input().split())
    G.add_edge(a - 1, b - 1)

for i in range(Q):
    pass

print(G.edges)
