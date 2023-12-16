N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

l1 = []
l2 = []
for ind, (c, r) in enumerate(zip(C, R)):
    if ind == 0:
        l1.append((r, ind + 1))
        col = c
    elif c == col:
        l1.append((r, ind + 1))
    if c == T:
        l2.append((r, ind + 1))

l1 = sorted(l1, key=lambda x: x[0], reverse=True)
l2 = sorted(l2, key=lambda x: x[0], reverse=True)

if l2:
    print(l2[0][1])
else:
    print(l1[0][1])