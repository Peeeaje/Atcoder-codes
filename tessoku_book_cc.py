N = input()

ans = 0
for i in range(len(N)):
    v = N[i]
    if v == '1':
        ans += 2 ** (len(N) - i - 1)

print(ans)
