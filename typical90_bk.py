H, W = map(int, input().split())
P = []

for i in range(H):
    P.append(list(map(int, input().split())))

ans = []
for i in range(2 ** H):
    R = dict()
    for j in range(H * W + 1):
        R[j] = 0

    array = []
    for j in range(H):
        if (i >> j) & 1:
            array.append(P[j])
        else:
            pass

    array = [list(x) for x in zip(*array)]

    for a in array:
        if len(set(a)) == 1:
            R[a[0]] += len(a)
    ans.append(max(R.values()))

print(max(ans))

