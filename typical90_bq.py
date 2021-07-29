N, K = map(int, input().split())
if N == 1:
    print(K)

elif N == 2 and K >= 2:
    print((K * (K-1)) % (10**9 + 7))

elif N >= 3 and K >= 3:
    print((K * (K - 1) * pow((K - 2), (N - 2), (10 ** 9 + 7))) % (10 ** 9 + 7))

else:
    print(0)