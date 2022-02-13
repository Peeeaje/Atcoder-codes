N, M = map(int, input().split())
S = list(input().split())
T = set(list(input().split()))

for value in S:
    print("Yes" if value in T else "No")
