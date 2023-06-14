import math

A, B = map(int, input().split())
gcd = math.gcd(A, B)
ans = A // gcd * B

if ans > 10**18:
    print("Large")
else:
    print(ans)
