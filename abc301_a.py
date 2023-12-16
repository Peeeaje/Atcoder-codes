n = int(input()) + 1
s = input()

a = 0
b = 0
for i in range(n - 1):
    if s[i] == 'T':
        a += 1
    else:
        b += 1

    if a == n // 2:
        print('T')
        exit()
    if b == n // 2:
        print('A')
        exit()