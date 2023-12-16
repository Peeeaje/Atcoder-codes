N = int(input())

for k in range(10000000):
    if k == 0:
        a = 1
    else:
        a *= 2
    if a > N:
        print(k - 1)
        exit()
