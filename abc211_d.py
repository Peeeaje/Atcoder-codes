import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


import collections
import heapq

class Dijkstra:
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d):
        self.e[u].append([v, d])
        self.e[v].append([u, d])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def search(self, s):
        """
        :param s: 始点
        :return: 始点から各点までの最短経路
        """
        ans=collections.defaultdict(lambda: float('inf'))
        d = collections.defaultdict(lambda: float('inf'))
        ans[s]=1
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] == vd:
                    ans[uv] += 1
                if d[uv] > vd:
                    ans[uv] = ans[vd]
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d, ans

G = Dijkstra()
N, M = from_readline()
for i in range(M):
    u,v = from_readline()
    G.add(u,v,1)
print(G.search(1))