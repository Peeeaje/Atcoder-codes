N = int(input())
A = list(map(int, input().split()))

ans = 0
for n in A:
    if n > 10:
        ans += n - 10
print(ans)
