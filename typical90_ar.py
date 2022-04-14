N, Q = map(int, input().split())
A = list(map(int, input().split()))

shifts = 0
for i in range(Q):
    t, x, y = map(int, input().split())
    x = (x - shifts - 1) % N
    y = (y - shifts - 1) % N

    if t == 1:
        A[x], A[y] = A[y], A[x]
    if t == 2:
        shifts += 1
    if t == 3:
        print(A[x])
