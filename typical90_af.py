import itertools

N = int(input())
A = list()
for i in range(N):
    A.append(list(map(int, input().split())))

M = int(input())
XY = list()
for i in range(M):
    XY.append(tuple(map(int, input().split())))
XY = set(XY)

ans = 10 ** 9
for i in itertools.permutations(range(N)):
    temp = 0
    for j in range(N - 1):
        if (
            tuple([i[j] + 1, i[j + 1] + 1]) in XY
            or tuple([i[j + 1] + 1, i[j] + 1]) in XY
        ):
            temp = 1

    if temp == 0:
        temp_ans = 0
        for k in range(N):
            temp_ans += A[i[k]][k]
        ans = min(ans, temp_ans)

print(-1 if ans == 10 ** 9 else ans)
