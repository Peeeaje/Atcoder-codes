n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(0, 7 * n, 7):
    ans.append(sum(a[i:i+7]))

print(*ans)