import math

N = int(input())
A = list(map(int, input().split()))
gcd = math.gcd(A[0], A[1])

for i in range(2, N):
    gcd = math.gcd(gcd, A[i])
print(gcd)
