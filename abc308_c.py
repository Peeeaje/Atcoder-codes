n = int(input())
l = []

for i in range(n):
    a, b = map(int, input().split())
    l.append((i, a, b))


l = sorted(l, key=lambda x: (x[1]/(x[1] + x[2]), -x[0]), reverse=True)
ans = [x[0] + 1 for x in l]
print(*ans)