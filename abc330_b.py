n, l, r = map(int, input().split())
a = list(map(int, input().split()))
m = (l + r) // 2

for i in range(n):
    a_i = a[i]
    trail = ' ' if i < n - 1 else ''
    if a_i < l:
        print(l, end=trail)
    elif a_i > r:
        print(r, end=trail)
    else:
        print(a_i, end=trail)

print()