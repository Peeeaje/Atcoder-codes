N, K = map(int, input().split())
l = []

for i in range(N):
    a, b = map(int, input().split())
    l.append([a, b])
# aについてソートする
l = sorted(l, key=lambda x: x[0])

for i in range(N):
    if K >= l[i][0]:
        K += l[i][1]
    else:
        break
print(K)
