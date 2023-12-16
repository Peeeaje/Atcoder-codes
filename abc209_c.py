N = int(input())
C = list(map(int, input().split()))
C = sorted(C)

ans = 1
for i in range(N):
    c = C[i] - i
    ans = (ans * c) % (10**9 + 7)
print(ans)
