import math

N = int(input())
graph = dict()

for i in range(N - 1):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)


def dfs(graph, v, distance, seen):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v] == 1:
            continue
        distance[next_v] = min(distance[v] + 1, distance[next_v])
        dfs(graph, next_v, distance, seen)


def return_distance(graph, v):
    seen = [0] * (N + 1)
    distance = [10000000] * (N + 1)
    distance[v] = 0
    dfs(graph, v, distance, seen)
    return distance


distance = return_distance(graph, 1)

temp_v = -1
temp_k = -1
for v in distance[1:]:
    if v > temp_v:
        temp_v = v
        temp_k = distance.index(temp_v)

distance = return_distance(graph, temp_k)[1:]

maxi = max(distance)

print(maxi + 1)
