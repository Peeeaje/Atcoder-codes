N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


def rotate(A):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[i][j] = A[N - j - 1][i]

    return res

def check(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] == 0:
                return False
    return True

for _ in range(4):
    if check(A, B):
        print('Yes')
        exit()
    A = rotate(A)

print('No')