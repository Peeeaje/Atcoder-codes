K, N = map(int, input().split())

ans = 0

for X in range(K + 1):
    for Y in range(K + 1):
        Z = N - X - Y
        if K >= Z >= 0:
            ans += 1
print(ans)
