N = int(input())

ans = "A"
for k in range(10000000):
    if k == 0:
        a = 1
    else:
        a *= 2
    if a > N:
        break
k -= 1
if k < 0:
    v = 0
else:
    v = 2 ** max(0, k)
print(ans + "B" * k + "A" * (N - v))
