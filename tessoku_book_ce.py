N = int(input())
A = list(map(int, input().split()))
cumsum_A = [0] * (N + 1)
for i in range(N):
    cumsum_A[i + 1] = cumsum_A[i] + A[i]

cumsum_B = [0] * (N + 1)
for i in range(N):
    cumsum_B[i + 1] = cumsum_B[i] + 1 - A[i]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    win = cumsum_A[R] - cumsum_A[L - 1]
    lose = cumsum_B[R] - cumsum_B[L - 1]
    if win > lose:
        print('win')
    elif win < lose:
        print('lose')
    else:
        print('draw')
