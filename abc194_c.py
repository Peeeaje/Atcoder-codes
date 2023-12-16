import collections
import itertools

d = collections.defaultdict(dict)

for a in range(-200, 201):
    for b in range(-200, 201):
        d[a][b] = (a - b) ** 2

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

ans = 0
for a, b in itertools.combinations(set(A), 2):
    ans += d[a][b] * c[a] * c[b]
print(ans)
