n, m, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [(a[i], i) for i in range(n)]
b = [(b[i], i) for i in range(m)]
sorted_a = sorted(a, reverse=True, key=lambda x: x[0])
sorted_b = sorted(b, reverse=True, key=lambda x: x[0])
dif_a = [sorted_a[i][0] - sorted_a[i + 1][0] for i in range(n - 1)]
dif_b = [sorted_b[i][0] - sorted_b[i + 1][0] for i in range(m - 1)]

print(dif_a)


s = set()
for i in range(l):
    c, d = map(int, input().split())
    s.add((c, d))

N = 0
M = 0

tmp = []
for i in range(n):
    for j in range(m):
        tmp.append(a[i][0] + b[j][0])
tmp = sorted(tmp, reverse=True)
print(tmp)


for i in range(10):
    # print(sorted_a[N][1] + 1, sorted_b[M][1] + 1)
    print(sorted_a[N][0] + sorted_b[M][0])
    if (sorted_a[N][1] + 1, sorted_b[M][1] + 1) in s:
        if dif_a[N] >= dif_b[M]:
            M += 1
        else:
            N += 1
    else:
        v = sorted_a[N][0] + sorted_b[M][0]
        # break
# print(v)

# ans = -1
# for i in range(n):
#     for j in range(m):
#         if (sorted_a[i][1] + 1, sorted_b[j][1] + 1) not in s:
#             ans = sorted_a[i][0] + sorted_b[j][0]
#             break
#     if ans != -1:
#         break

# for j in range(m):
#     for i in range(n):
#         if (sorted_a[i][1] + 1, sorted_b[j][1] + 1) not in s:
#             ans = max(ans, sorted_a[i][0] + sorted_b[j][0])
#             break
#     if ans != -1:
#         break

# print(ans)