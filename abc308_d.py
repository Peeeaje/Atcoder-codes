from collections import deque

d = {'s': 'n', 'n': 'u', 'u': 'k', 'k': 'e', 'e' : 's'}

def nxt(i, j):
    if S[i][j] not in d:
        return

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue


        if d[S[i][j]] == S[ni][nj]:
            yield ni, nj

def bfs(i, j):
    q = deque([(i, j)])
    visited = [[False] * w for _ in range(h)]
    visited[i][j] = True
    while q:
        i, j = q.popleft()
        for ni, nj in nxt(i, j):
            if visited[ni][nj]:
                continue
            q.append((ni, nj))
            visited[ni][nj] = True

    return visited


h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
visited = bfs(0, 0)

if visited[h - 1][w - 1]:
    print('Yes')
else:
    print('No')

