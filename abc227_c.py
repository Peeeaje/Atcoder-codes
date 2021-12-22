N = int(input())

ans = 0
for a in range(1, N + 1):
    for b in range(a, N + 1):
        c_lower = N // (a * b)
        if c_lower >= b:
            ans += c_lower - b + 1
            print(a, b, c_lower)
print(ans)

