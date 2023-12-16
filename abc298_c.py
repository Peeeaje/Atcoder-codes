import collections

import sortedcontainers

N = int(input())
Q = int(input())
boxes = collections.defaultdict(sortedcontainers.SortedList)
cards = collections.defaultdict(sortedcontainers.SortedSet)


for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i, j = q[1], q[2]
        boxes[j].add(i)
        cards[i].add(j)
    if q[0] == 2:
        i = int(q[1])
        print(*boxes[i])
    if q[0] == 3:
        i = int(q[1])
        print(*cards[i])
