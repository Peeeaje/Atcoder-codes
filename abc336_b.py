n = bin(int(input()))

ans = 0
for i in range(len(n)):
    if n[- i - 1] == '0':
        ans += 1
    else:
        print(ans)
        exit()


