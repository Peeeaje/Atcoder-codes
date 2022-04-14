H, W = map(int, input().split())
P = []

for i in range(H):
    P.append(list(map(int, input().split())))

for i in range(2**H):
    rows = []
    for j in range(H):
        if i >> j & 1:
            rows.append(P[j])
    same_columns = []
    rows_T = list(zip(*rows))

    for value in rows_T:
        if len(set(value)) == 1:
            same_columns.append(value[0])
