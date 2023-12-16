n = int(input())
a = list(map(int, input().split()))
l = [0]
max_ = float('-inf')
for i in range(n):
    a_i = a[i]
    max_ = max(max_, a_i)
    l.append(max_)

r = [0]
max_ = float('-inf')
for i in range(n - 1, -1, -1):
    a_i = a[i]
    max_ = max(max_, a_i)
    r.append(max_)

r = r[::-1]
d = int(input())

for _ in range(d):
    L, R = map(int, input().split())
    print(max([l[L - 1], r[R]]))
