from math import factorial

P = int(input())

ans = 0
for i in range(10, 0, -1):
    ans += P // factorial(i)
    P = P % factorial(i)
print(ans)
