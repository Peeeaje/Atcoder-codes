import collections

N = int(input())
a = list(map(int, input().split()))
d = collections.deque()

count = 0
for val in a:
    if len(d) == 0:
        d.append([a[0], 1])
        count += 1
        print(count)
        continue

    last = d[-1]

    if last[0] != val:
        d.append([val, 1])
        count += 1
    else:
        temp = d.pop()
        d.append([temp[0], temp[1] + 1])
        last = d[-1]
        count += 1

        if last[0] == last[1]:
            count -= last[0]
            d.pop()

    print(count)
