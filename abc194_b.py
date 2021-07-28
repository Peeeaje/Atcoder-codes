from abc import ABCMeta


N = int(input())
AB = []
A = []
B = []

for i in range(N):
    AB.append(list(map(int, input().split())))

for i in range(N):
    A.append(AB[i][0])

for i in range(N):
    B.append(AB[i][0])

ans = 100000000000

for i in range(N):
    for j in range(N):
        ans = min(ans, AB[i][0] + AB[j][1])
        if i != j:
            ans = min(max(AB[i][0], AB[j][1]), ans)

print(ans)
