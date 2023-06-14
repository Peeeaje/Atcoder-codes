N = int(input())

A = []
for i in range(N):
    t, l, r = map(int, input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    A.append((l, r))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        l_i, r_i = A[i]
        l_j, r_j = A[j]
        if l_j <= r_i and l_i <= r_j:
            ans += 1
print(ans)
