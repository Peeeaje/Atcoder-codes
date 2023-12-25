n, m = map(int, input().split())
l_p, l_c, l_f = [], [], []
for i in range(n):
    p, c, *f = map(int, input().split())
    l_p.append(p)
    l_c.append(c)
    l_f.append(set(f))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if l_p[i] < l_p[j]:
            continue
        if len(l_f[i] - l_f[j]) > 0:
            continue
        if l_p[i] > l_p[j]:
            print("Yes")
            exit()
        if len(l_f[j] - l_f[i]) > 0:
            print("Yes")
            exit()

print("No")
