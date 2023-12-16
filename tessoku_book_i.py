H, W, N = map(int, input().split())
field = [[0] * (W + 1) for _ in range(H + 1)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    field[a - 1][b - 1] += 1
    field[a - 1][d] -= 1
    field[c][b - 1] -= 1
    field[c][d] += 1

for i in range(H):
    for j in range(1, W):
        field[i][j] += field[i][j - 1]

for i in range(1, H):
    for j in range(W):
        field[i][j] += field[i - 1][j]

for v in field[:-1]:
    print(*v[:-1])
