n = int(input())
S = []
for i in range(n):
    S.append(list(input()))

h = [0] * n
for i in range(n):
    for j in range(n):
        if S[i][j] == 'o':
            h[i] += 1
w = [0] * n
for i in range(n):
    for j in range(n):
        if S[j][i] == 'o':
            w[i] += 1

ans = 0
for i in range(n):
    for j in range(n):
        if S[i][j] == 'x':
            continue
        ans += (h[i] - 1) * (w[j] - 1)

print(ans)