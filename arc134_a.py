N, L, W = map(int, input().split())
a = list(map(int, input().split()))

l = [[0, a[0]]]

left = a[0]
right = 0
for i in range(len(a) - 1):
    left = a[i]
    right = a[i + 1]
    if right - left > W:
        l.append([left + W, right])

if right + W < L:
    l.append([right + W, L])

ans = 0
for left, right in l:
    space = right - left
    ans += (space - 1) // W + 1

print(ans)
