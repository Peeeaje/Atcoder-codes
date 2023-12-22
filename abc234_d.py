from sortedcontainers import SortedList

n, k = map(int, input().split())
a = list(map(int, input().split()))

l = SortedList(a[:k])
print(l[-k])

for i in range(k, n):
    l.add(a[i])
    print(l[-k])
