x1, y1, x2, y2 = map(int, input().split())


def ret_candidates(x, y):
    for div_x, div_y in [[-2, 1], [-1, 2], [1, 2], [2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]:
        yield x + div_x, y + div_y

l1 = ret_candidates(x1, y1)
l2 = set(ret_candidates(x2, y2))

for i in l1:
    if i in l2:
        print("Yes")
        exit()
print("No")