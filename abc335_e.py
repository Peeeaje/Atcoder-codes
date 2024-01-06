from collections import deque


n, m = map(int, input().split())
a = list(map(int, input().split()))

edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())

    if a[u - 1] <= a[v - 1]:
        edges[u - 1].append(v - 1)

    if a[v - 1] <= a[u - 1]:
        edges[v - 1].append(u - 1)

scores = [-1] * n
scores[0] = 1

# bfs
q = deque([0])

while q:
    u = q.popleft()
    for v in edges[u]:
        if a[u] == a[v]:
            score = scores[u]
        else:
            score = scores[u] + 1

        if scores[v] == -1 or scores[v] < score:
            scores[v] = score
            q.append(v)

if scores[-1] == -1:
    print(0)
else:
    print(scores[-1])
