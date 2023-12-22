from sortedcontainers import SortedSet

x = int(input())
s = SortedSet()

# 等差が0でないものを列挙する
for a in range(1, 10):
    for d in range(-9, 10):
        if d == 0:
            continue
        t = ""
        for n in range(0, 10):
            if a + d * n < 0 or a + d * n > 9:
                break
            t += str(a + d * n)
            s.add(int(t))

for a in range(1, 10):
    for j in range(2, 20):
        s.add(int(str(a) * j))


print(s[s.bisect_left(x)])
