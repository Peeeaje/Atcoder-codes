import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))

a_left = a[:n // 2]
a_right = a[n // 2:]

s1 = set([0])
for i in range(1, len(a_left) + 1):
    for c in itertools.combinations(a_left, i):
        s1.add(sum(c))

s2 = set([0])
for i in range(1, len(a_right) + 1):
    for c in itertools.combinations(a_right, i):
        s2.add(sum(c))

for v in s1:
    if k - v in s2:
        print('Yes')
        exit()

print('No')