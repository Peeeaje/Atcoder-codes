from collections import defaultdict

N = int(input())
d = defaultdict(dict)
l = []

for _ in range(N):
    X, Y = map(int, input().split())
    l.append((X, Y))
S = input()

for i in range(N):
    X, Y = l[i]
    direction = S[i]
    if d[Y].get(direction, None) is None:
        d[Y][direction] = X
    else:
        if direction == "L":
            d[Y][direction] = max(d[Y][direction], X)
        else:
            d[Y][direction] = min(d[Y][direction], X)

for k, v in d.items():
    l = v.get("L", None)
    r = v.get("R", None)

    if l is not None and r is not None:
        if l > r:
            print("Yes")
            exit()
print("No")
