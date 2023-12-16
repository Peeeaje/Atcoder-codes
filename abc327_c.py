A = [list(map(int, input().split())) for _ in range(9)]

#  行について確認
for row in A:
    if len(set(row)) != 9:
        print("No")
        exit()

# 列について確認
for col in zip(*A):
    if len(set(col)) != 9:
        print("No")
        exit()

# 3x3のブロックについて確認
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        block = A[i][j : j + 3] + A[i + 1][j : j + 3] + A[i + 2][j : j + 3]
        if len(set(block)) != 9:
            print("No")
            exit()
print("Yes")
