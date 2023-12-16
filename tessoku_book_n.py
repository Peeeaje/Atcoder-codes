n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

s1 = set()
for i in range(n):
    for j in range(n):
        a_i = a[i]
        b_j = b[j]
        s1.add(a_i + b_j)

s2 = set()
for i in range(n):
    for j in range(n):
        c_i = c[i]
        d_j = d[j]
        s2.add(c_i + d_j)


for v in s1:
    if k - v in s2:
        print('Yes')
        exit()
print('No')