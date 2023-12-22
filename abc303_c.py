n, m, h, k = map(int, input().split())
S = input()

li = set()
for _ in range(m):
    x, y = map(int, input().split())
    li.add((x, y))

cord = [0, 0]
for s in S:
    if s == "U":
        cord[1] += 1
    elif s == "D":
        cord[1] -= 1
    elif s == "L":
        cord[0] -= 1
    elif s == "R":
        cord[0] += 1

    h -= 1
    if h < 0:
        print("No")
        exit()
    if tuple(cord) in li and h < k:
        h = k
        li.remove(tuple(cord))
print("Yes")
