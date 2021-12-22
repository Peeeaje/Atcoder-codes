import sys

sys.setrecursionlimit(300000)


def dfs(G, v):
    for next_v in G[v]:
        if seen[next_v] != -1:
            continue
        else:
            seen[next_v] = seen[v] + 1
        dfs(G, next_v)


N = int(input())

graph = dict()
for i in range(N + 1):
    graph[i] = []

for i in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

seen = [-1] * (N + 1)
seen[1] = 0
dfs(graph, 1)

max_node = seen.index(max(seen))
seen = [-1] * (N + 1)
seen[max_node] = 0
dfs(graph, max_node)
print(max(seen) + 1)
