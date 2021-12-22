import sys

sys.setrecursionlimit(300000)
N = int(input())

G = dict()
for i in range(1, N + 1):
    G[i] = []

for i in range(N - 1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

col = [-1] * (N + 1)
col[1] = 0

seen = [0] * (N + 1)


def dfs(G, v):
    seen[v] = True

    for next_v in G[v]:
        if seen[next_v] == 1:
            continue
        dfs(G, next_v)


def dfs(G, v, cur):
    seen[v] = True

    for next_v in G[v]:
        if seen[next_v] == 1:
            continue
        col[next_v] = 1 - cur
        dfs(G, next_v, col[next_v])


seen = [0] * (N + 1)
dfs(G, 1, 0)
col = col[1:]

temp_0 = sum([1 for i in col if i == 0])
temp_1 = sum([1 for i in col if i == 1])

if temp_0 > temp_1:
    ans = []
    for i in range(len(col)):
        if col[i] == 0:
            ans.append(str(i + 1))
else:
    ans = []
    for i in range(len(col)):
        if col[i] == 1:
            ans.append(str(i + 1))

print(" ".join(ans[: N // 2]))
