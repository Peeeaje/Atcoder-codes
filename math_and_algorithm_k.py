N = int(input())

s = set()
for i in range(2, N + 1):
    for j in range(2, N // i + 1):
        s.add(i * j)

ans = []
for i in range(2, N + 1):
    if i not in s:
        ans.append(i)
print(" ".join(map(str, ans)))
