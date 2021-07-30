L, R = map(int, input().split())

lenL = len(str(L))
lenR = len(str(R))

ans = 0

for i in range(lenL,lenR+1):
    if lenL == lenR:
        n = R - L + 1
        l = L
        r = R
        ans += ((n * (l + r)) * i //2)

    elif i == lenL:
        n = 10 ** lenL - L
        l = L
        r = 10 ** lenL - 1
        ans += ((n * (l + r)) * i //2)
    
    elif i == lenR:
        n = R - 10 ** (lenR-1) + 1
        l = 10 ** (lenR - 1)
        r = R
        ans += ((n * (l + r)) * i //2)
    
    else:
        n = 10 ** i - 10 ** (i-1)
        l = 10 ** (i - 1)
        r = 10 ** i - 1
        ans += ((n * (l + r)) * i //2)

print(ans % (10**9 + 7))