from sortedcontainers import SortedSet

d = int(input())

s = SortedSet()
for i in range(int(d ** 0.5) + 1):
    s.add(i ** 2)

ans = float('inf')
for a in s:
    b = abs(a - d)
    index = s.bisect_left(b)
    if index == 0:
        ans = min([ans, abs(a + s[index] - d)])
        continue
    if index == len(s):
        ans = min([ans, abs(a + s[index - 1] - d)])
        continue

    ans = min([ans, abs(a + s[index] - d), abs(a + s[index - 1] - d)])

print(ans)