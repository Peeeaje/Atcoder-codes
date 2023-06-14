A, B, C, D = map(int, input().split())

if B >= C * D:
    print(-1)
    exit()

for i in range(10**6):
    if A + B * i <= C * D * i:
        print(i)
        exit()
