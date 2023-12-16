N = int(input())
MAX = 1501
m = [[0] * MAX for _ in range(MAX)]
for i in range(N):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    m[x][y] += 1

cumsum = [[0] * (MAX + 1) for _ in range(MAX + 1)]
for i in range(MAX):
    for j in range(MAX):
        cumsum[i + 1][j + 1] = cumsum[i + 1][j] + cumsum[i][j + 1] - cumsum[i][j] + m[i][j]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(cumsum[c][d] - cumsum[a - 1][d] - cumsum[c][b - 1] + cumsum[a - 1][b - 1])
