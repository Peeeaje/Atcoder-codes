n, l = map(int, input().split())
a = list(map(int, input().split()))

print(sum(1 if v >= l else 0 for v in a))