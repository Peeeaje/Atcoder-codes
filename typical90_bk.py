import collections

H, W = map(int, input().split())
P = []

for i in range(H):
    P.append(list(map(int, input().split())))

ans = 0
for i in range(2**H):
    selected_rows = []
    for j in range(H):
        if i >> j & 1:
            selected_rows.append(P[j])

    valid_column_headers = []
    rows_T = list(zip(*selected_rows))
    for value in rows_T:
        if len(set(value)) == 1:
            valid_column_headers.append(value[0])

    temp_ans = 0
    if len(valid_column_headers) != 0:
        temp_ans += (
            collections.Counter(valid_column_headers).most_common()[0][1]
        ) * len(selected_rows)
    ans = max(ans, temp_ans)
print(ans)
