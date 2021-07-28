H, W = map(int, input().split())
A = list()

for i in range(H):
    A.append(list(map(int, input().split())))

sum_H = list()
sum_W = list()

for i in A:
    sum_H.append(sum(i))

for i in list(zip(*A)):
    sum_W.append(sum(i))

ans = [[0 for i in range(W)] for j in range(H)]

for i in range(H):
    for j in range(W):
        ans[i][j] = sum_H[i] + sum_W[j] - A[i][j]

for i in ans:
    print(*i)