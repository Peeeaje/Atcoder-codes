H, W = map(int, input().split())
A = list()

for i in range(H):
    A.append(list(map(int, input().split())))

l = [[0] * W for i in range(H)]

sum_v = list()
for i in range(W):
    sum_v.append(sum([a[i] for a in A]))

sum_h = list()
for i in range(H):
    sum_h.append(sum(A[i][:]))


for i in range(H):
    for j in range(W):
        l[i][j] = sum_v[j] + sum_h[i] - A[i][j]

for i in l:
    print(*i)