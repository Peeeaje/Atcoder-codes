N, Q = map(int, input().split())
S = input()
T = [0]
tmp = 0
for i in range(1, N):
    if S[i - 1] == S[i]:
        tmp += 1
        T.append(tmp)
    else:
        T.append(tmp)

for _ in range(Q):
    a, b = map(int, input().split())
    print(T[b - 1] - T[a - 1])
