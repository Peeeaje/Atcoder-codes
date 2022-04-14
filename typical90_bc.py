N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] = A[i] % P


ans = 0
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            for d in range(c + 1, N):
                for e in range(d + 1, N):
                    if A[a] % P * A[b] % P * A[c] % P * A[d] % P * A[e] % P == Q:
                        ans += 1

print(ans)
