a = list(map(int, input().split()))

ans = 0
for i in range(len(a)):
    ans += 2 ** i * a[i]

print(ans)