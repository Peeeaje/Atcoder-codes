N = int(input())
A, B, C = map(int, input().split())
ans = 10 ** 10

for x in range(10000):
    for y in range(9999 - x):
        k = N - (A * x + B * y)
        if k % C == 0 and k >= 0:
            ans = min(ans, x + y + k // C)
print(ans)