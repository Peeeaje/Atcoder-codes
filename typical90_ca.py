def change_square(matrix: list, a: int, b: int, div: int):
    for x in [0, 1]:
        for y in [0, 1]:
            matrix[a + x][b + y] += div


H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
B = []
for i in range(H):
    B.append(list(map(int, input().split())))

c = 0
for a in range(H - 1):
    for b in range(W - 1):
        if A[a][b] == B[a][b]:
            continue
        else:
            div = B[a][b] - A[a][b]
            change_square(A, a, b, div)
            c += abs(div)
if A == B:
    print("Yes")
    print(c)
else:
    print("No")
