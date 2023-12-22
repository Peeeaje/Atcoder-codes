n, m = map(int, input().split())
rels = [set(range(n)) - set([i]) for i in range(n)]


for _ in range(m):
    a = list(map(int, input().split()))
    for i in range(1, len(a)):
        before = a[i - 1] - 1
        current = a[i] - 1

        if before in rels[current]:
            rels[current].remove(before)
        if current in rels[before]:
            rels[before].remove(current)

ans = 0
for i in range(n):
    ans += len(rels[i])

print(ans // 2)
