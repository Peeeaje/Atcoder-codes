T = int(input())
N = int(input())

l = [0] * (T + 1)
for i in range(N):
    L, R = map(int, input().split())
    l[L] += 1
    l[R] -= 1

cumsum = [0] * (T + 1)
for i in range(T):
    cumsum[i + 1] = cumsum[i] + l[i]

for v in cumsum[1:]:
    print(v)