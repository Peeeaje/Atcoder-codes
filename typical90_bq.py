N, K = map(int, input().split())
ans = 0

if N >= 1:
    ans += K
if N >= 2:
    ans *= K - 1
if N >= 3:
    ans *= pow(K - 2, N - 2, (10**9 + 7))
print(ans % (10**9 + 7))
