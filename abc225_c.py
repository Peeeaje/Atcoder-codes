N, M = map(int, input().split())
B0 = list(map(int, input().split()))

for i in range(1, M):
    if (B0[0] + i != B0[i]) or (i != M - 1 and B0[i] % 7 == 0):
        print("No")
        exit()

for i in range(1, N):
    if list(map(lambda x: x + i * 7, B0)) != list(map(int, input().split())):
        print("No")
        exit()

print("Yes")
