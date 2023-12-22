h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]


def next(i, j):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < h and 0 <= ny < w and S[nx][ny] == ".":
            yield nx, ny, 0

    for dx in [-2, -1, 0, 1, 2]:
        for dy in [-2, -1, 0, 1, 2]:
            if dx == dy == 0:
                continue
            if abs(dx) + abs(dy) == 4:
                continue
            nx, ny = i + dx, j + dy
            if 0 <= nx < h and 0 <= ny < w and S[nx][ny] != ".":
                yield nx, ny, 1


from collections import deque

q = deque([(0, 0, 0)])
dist = [[-1] * w for _ in range(h)]
dist[0][0] = 0
while q:
    i, j, c = q.popleft()
    for ni, nj, nc in next(i, j):
        if dist[ni][nj] == -1:
            dist[ni][nj] = dist[i][j] + nc
            if nc == 0:
                q.appendleft((ni, nj, nc))
            else:
                q.append((ni, nj, nc))

print(dist[h - 1][w - 1])
