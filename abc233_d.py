import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))
A_cumsum = [0]
for i in range(N):
    A_cumsum.append(A[i] + A_cumsum[i])

c = collections.Counter(A_cumsum)

ans = 0
for i in range(N):
    left = A_cumsum[i]
    right = K + left
    ans += c[right]
    c[left] -= 1
print(ans)

