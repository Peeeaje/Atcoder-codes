n, a, b = map(int, input().split())
c = list(map(int, input().split()))

for i in range(n):
    c_i = c[i]
    if c_i == a + b:
        print(i + 1)
        exit()