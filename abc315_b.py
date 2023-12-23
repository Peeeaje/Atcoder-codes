m = int(input())
d = list(map(int, input().split()))

mid = sum(d) // 2 + 1

for i in range(m):
    if mid > d[i]:
        mid -= d[i]
    else:
        print(i + 1, mid)
        exit()