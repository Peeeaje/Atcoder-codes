import sys
sys.setrecursionlimit(300000)

N = int(input())

G = [[] for i in range(N+1)]

for i in range(N-1):
    temp1, temp2 = map(int, input().split())
    G[temp1].append(temp2)
    G[temp2].append(temp1)

G = [sorted(i) for i in G]

seen = [0] * (N+1)
ans = []

def dfs(G, v):
    seen[v] = True
    ans.append(v)
    for next_v in G[v]:
        if seen[next_v] == 1:
            continue
        dfs(G, next_v)
        ans.append(v)
    return ans
print(*dfs(G, 1))