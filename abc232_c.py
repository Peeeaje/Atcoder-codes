import itertools
import copy


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)


N, M = map(int, input().split())
G1 = Graph(N)
G2 = Graph(N)

for i in range(M):
    u, v = map(int, input().split())
    G1.add_edge(u - 1, v - 1)

for i in range(M):
    u, v = map(int, input().split())
    G2.add_edge(u - 1, v - 1)


former = [*range(N)]
for later in itertools.permutations([*range(N)]):
    dic = dict(zip(former, later))
    g = Graph(N)
    # print(dic)

    for i in range(N):
        to_edges = G2.edges[i]
        frm_converted = dic[i]
        for v in to_edges:
            to_converted = dic[v]
            g.edges[frm_converted].append(to_converted)
            
        g.edges[frm_converted].sort()
    if g.edges == G1.edges:
        print("Yes")
        exit()
print("No")
