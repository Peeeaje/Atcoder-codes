import collections

N = int(input())


array = [[0] * 1002 for i in range(1002)]
count = [0] * (N + 1)


for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    array[lx][ly] += 1
    array[rx][ry] += 1
    array[lx][ry] -= 1
    array[rx][ly] -= 1

for i in range(1000):
    for j in range(1000):
        array[i][j] += array[i][j - 1]

for i in range(1000):
    for j in range(1000):
        array[i][j] += array[i - 1][j]
        count[array[i][j]] += 1

for i in count[1:]:
    print(i)
