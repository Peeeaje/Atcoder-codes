N = int(input())
S = input()
s = set(S)

if 'o' not in s or '-' not in s:
    print(-1)
    exit()

ans = 0
tmp = 0
for s in S:
    if s == '-':
        ans = max(ans, tmp)
        tmp = 0
    else:
        tmp += 1

ans = max(ans, tmp)
print(ans)

