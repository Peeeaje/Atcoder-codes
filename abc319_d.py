n, m = map(int, input().split())
L = list(map(int, input().split()))


def judge(w):
    width, height = 0, 0

    for i in range(n):
        if i == 0:
            width = L[i]
            height += 1
            continue

        if width + L[i] + 1 > w:
            width = L[i]
            height += 1
        else:
            width += L[i] + 1

    return height <= m


l = max(L) - 1
r = 10**15

while r - l > 1:
    mid = (l + r) // 2
    if judge(mid):
        r = mid
    else:
        l = mid

print(r)
