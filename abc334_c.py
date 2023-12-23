n, k = map(int, input().split())
a = list(map(int, input().split()))

if k % 2 == 0:
    ans = 0
    for i in range(0, k, 2):
        ans += a[i + 1] - a[i]
else:
    fr = [0] * (k // 2)
    ba = [0] * (k // 2)
    for i in range(k - 1):
        if i % 2 == 0:
            fr[i // 2] = a[i + 1] - a[i]
        else:
            ba[i // 2] = a[i + 1] - a[i]
    for i in range(1, k // 2):
        fr[i] += fr[i - 1]
        ba[-1 - i] += ba[-i]
    fr = [0] + fr
    ba = ba + [0]

    ans = float("inf")
    for i in range(len(fr)):
        ans = min(ans, fr[i] + ba[i])
    if ans == float("inf"):
        ans = 0
print(ans)
