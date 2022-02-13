import math

n, r = map(int, input().split())

ans = math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
print(ans)
