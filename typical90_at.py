import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(N):
    A[i] %= 46
    B[i] %= 46
    C[i] %= 46

c_A = collections.Counter(A)
c_B = collections.Counter(B)
c_C = collections.Counter(C)

ans = 0
for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a + b + c) % 46 == 0:
                ans += c_A[a] * c_B[b] * c_C[c]
print(ans)
