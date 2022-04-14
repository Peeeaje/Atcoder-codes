N, Q = map(int, input().split())
A = list(map(int, input().split()))
dif_A = []
for i in range(1, len(A)):
    dif_A.append(A[i] - A[i - 1])
ans = sum([abs(n) for n in dif_A])
for i in range(Q):
    left, right, v = map(int, input().split())
    div = 0
    if left >= 2:
        temp = dif_A[left - 2]
        dif_A[left - 2] += v
        div += abs(dif_A[left - 2]) - abs(temp)

    if right <= N - 1:
        temp = dif_A[right - 1]
        dif_A[right - 1] -= v
        div += abs(dif_A[right - 1]) - abs(temp)
    ans += div

    print(ans)
