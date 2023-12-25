import copy

n = int(input())
a = [list(input()) for _ in range(n)]
b = copy.deepcopy(a)

for i in range(n):
    for j in range(n):
        if i == 0 and j != 0:
            b[i][j] = a[i][j - 1]
        if i == n - 1 and j != n - 1:
            b[i][j] = a[i][j + 1]
        if j == 0 and i != n - 1:
            b[i][j] = a[i + 1][j]
        if j == n - 1 and i != 0:
            b[i][j] = a[i - 1][j]

for i in range(n):
    print("".join(b[i]))
