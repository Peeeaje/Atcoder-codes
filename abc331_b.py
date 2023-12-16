n, s, m, l = map(int, input().split())
a, b, c = s/6, m/8, l/12

ans = float('inf')

for i in range(20):
    for j in range(20):
        for k in range(20):
            tmp = i * s + j * m + k * l
            if i * 6 + j * 8 + k * 12 >= n:
                ans = min(ans, tmp)

print(ans)