import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())


cumsum = [0] * (n + 1)
for i in range(1, n):
    if i % 2 == 0:
        cumsum[i + 1] = cumsum[i] + a[i] - a[i - 1]
    else:
        cumsum[i + 1] = cumsum[i]
cumsum = cumsum[1:]


def time(t):
    ind = bisect.bisect_left(a, t)
    if ind % 2 == 1:
        return cumsum[ind]
    else:
        return cumsum[ind] + (t - a[ind])


for _ in range(q):
    l, r = map(int, input().split())
    print(time(r) - time(l))
