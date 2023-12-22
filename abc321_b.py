from sortedcontainers import SortedList

n, x = map(int, input().split())
a = SortedList(map(int, input().split()))

ans = -1
for i in range(101):
    b = a.copy()
    b.add(i)

    if sum(b[1:-1]) >= x:
        ans = i
        break

print(ans)

