N = int(input())
coordinates = []
coordinate_field = [[0] * (1002) for _ in range(1002)]
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    lt = (lx, ly)
    rt = (rx, ly)
    lb = (lx, ry)
    rb = (rx, ry)
    coordinate_field[lx][ly] += 1
    coordinate_field[rx + 1][ly] -= 1
    coordinate_field[lx][ry + 1] += 1
    coordinate_field[rx + 1][ry + 1] -= 1
