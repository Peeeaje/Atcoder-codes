n = input()
ans = n
for i in range(1, len(n)):
    n = n[:-1]
    ans = add(ans, n)

print(ans)