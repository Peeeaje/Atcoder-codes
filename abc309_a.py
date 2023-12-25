a, b = map(int, input().split())

if b - a == 1 and b in set([2, 3, 5, 6, 8, 9]):
    print("Yes")
else:
    print("No")