import collections

N, Q = map(int, input().split())
A = list(map(int, input().split()))

d = collections.defaultdict(list)
for i in range(len(A)):
    a = A[i]
    d[a].append(i + 1)

for i in range(Q):
    x, k = map(int, input().split())
    if len(d[x]) - 1 < k - 1:
        print(-1)

    else:
        print(d[x][k - 1])
