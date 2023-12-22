n = int(input())

s = ''

for i in range(n + 1):
    v = '-'
    for j in range(1, 10):
        if n % j != 0:
            continue
        if i % (n // j) == 0:
            v = str(j)
            break
    s += v

print(s)