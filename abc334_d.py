from sortedcontainers import SortedList

n, q = map(int, input().split())
r = sorted(list(map(int, input().split())))
cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = cumsum[i] + r[i]

cumsum = SortedList(cumsum)
for _ in range(q):
    x = int(input())
    i = cumsum.bisect_right(x)
    print(i - 1)