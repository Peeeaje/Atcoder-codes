L, R = map(int, input().split())
L_len = len(str(L))
R_len = len(str(R))

ans = 0
if L_len == R_len:
    a, b, l = L, R, L_len
    ans += ((a + b) * (b - a + 1) // 2) * l
else:
    for l in range(L_len, R_len + 1):
        if l == L_len:
            a, b = L, 10**l - 1
        elif l == R_len:
            a, b = 10 ** (l - 1), R
        else:
            a, b = 10 ** (l - 1), 10**l - 1

        ans += ((a + b) * (b - a + 1) // 2) * l

print(ans % (10**9 + 7))
