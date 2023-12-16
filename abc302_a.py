a, b = map(int, input().split())

if a % b == 0:
    tmp = 0
else:
    tmp = 1

print(a // b + tmp)