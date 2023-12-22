h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

l, r, u, d = float("inf"), -float("inf"), float("inf"), -float("inf")
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            l = min(l, j)
            r = max(r, j)
            u = min(u, i)
            d = max(d, i)

for i in range(u, d + 1):
    for j in range(l, r + 1):
        if S[i][j] != "#":
            print(i + 1, j + 1)
            exit()