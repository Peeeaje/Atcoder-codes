N, M = map(int, input().split())


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, a, b, w):
        self.edges[a].append((b, w))
        self.edges[b].append((a, w))

    def dijkstra(self, start):
        from heapq import heappop, heappush
        dist = [float('inf')] * self.n
        dist[start] = 0
        q = [(0, start)]
        while q:
            _, u = heappop(q)
            for v, w in self.edges[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heappush(q, (dist[v], v))
        return dist


g = Graph(N)
for _ in range(M):
    a, b, c = map(int, input().split())
    g.add_edge(a - 1, b - 1, c)

dist_1 = g.dijkstra(0)
dist_2 = g.dijkstra(N - 1)
for k in range(N):
    print(dist_1[k] + dist_2[k])