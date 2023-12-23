a, m, l, r = map(int, input().split())

x = (r - a)
y = (l - a)

# x, yの間に、mで割り切れる数がいくつあるかを求める
s = x // m
t = (y + m - 1) // m
print((s - t) + 1)

# x = 10, y = 5, m = 3
# x = 9, y = 6, m = 3