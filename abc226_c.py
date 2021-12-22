import sys

sys.setrecursionlimit(300000)


N = int(input())

A = []
T = []
K = []
for i in range(N):
    TKA = list(map(int, input().split()))
    T.append(TKA[0])
    K.append(TKA[1])
    A.append(TKA[2:])

todo = [N]


def put_todo(ind, A):
    todo.extend(A[ind])
    return A[ind]


def main(index):
    for ind in put_todo(index - 1, A):
        main(ind)


main(N)
ans = 0
for i in todo:
    ans += T[i - 1]

print(ans)
