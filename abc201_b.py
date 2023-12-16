N = int(input())
S = []

for i in range(N):
    s, t = input().split()
    t = int(t)
    S.append([s, t])

S.sort(key=lambda x: x[1], reverse=True)
print(S[1][0])
