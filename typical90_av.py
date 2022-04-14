N, K = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.extend((b, a - b))
print(sum(sorted(AB, reverse=True)[:K]))
