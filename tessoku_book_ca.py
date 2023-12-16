A, B = map(int, input().split())
for v in range(A, B + 1):
    if 100 % v == 0:
        print('Yes')
        exit()

print('No')