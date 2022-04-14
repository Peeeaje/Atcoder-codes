import itertools

N = int(input())
coordinates = []
for i in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

ans = 0
for iter in itertools.combinations(range(N), 3):
    x1, y1 = coordinates[iter[0]]
    x2, y2 = coordinates[iter[1]]
    x3, y3 = coordinates[iter[2]]

    if (y1 - y2) * (x1 - x3) != (x1 - x2) * (y1 - y3):
        ans += 1
print(ans)
