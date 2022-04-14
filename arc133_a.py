N = int(input())
A = list(map(int, input().split()))

B = [A[0]]
for i in range(N):
    if B[-1] != A[i]:
        B.append(A[i])
del_tar = A[0]

for i in range(1, len(B)):
    if B[i - 1] > B[i]:
        del_tar = B[i - 1]
        break
    del_tar = B[-1]
A = [x for x in A if x != del_tar]

print(" ".join(map(str, A)))