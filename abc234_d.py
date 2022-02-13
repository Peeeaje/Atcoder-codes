N, K = map(int, input().split())
P = list(map(int, input().split()))

l = sorted(P[:K])
n = l[-K]
print(n)
for i in range(K, N):
    print(P[i], n)
    if P[i] < n:
        n = min(P[i], l[-K + 1])
    # print(n)
