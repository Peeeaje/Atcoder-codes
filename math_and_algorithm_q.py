import math

N = int(input())
l = list(map(int, input().split()))

lcm = l[0] * l[1] // math.gcd(l[0], l[1])

for i in range(2, N):
    lcm = lcm * l[i] // math.gcd(lcm, l[i])


print(lcm)
